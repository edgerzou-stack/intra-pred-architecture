import graphviz
import os

# Set working directory to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Create the top-level directed graph
dot = graphviz.Digraph(comment='IPD 与 RDO 核心计算环路', format='svg', engine='dot')
dot.attr(rankdir='TB', splines='spline', nodesep='1.0', ranksep='0.8', pad='0.3', fontname='Helvetica, Arial, sans-serif')

# Create the subgraph
with dot.subgraph(name='cluster_Loop') as c:
    c.attr(label='IPD 与 RDO 核心计算环路', style='filled, rounded', fillcolor='#ffffe0', color='#fbc02d', penwidth='2', fontname='Helvetica, Arial, sans-serif', fontsize='20', margin='20')
    
    # Global node style
    c.attr('node', shape='box', style='filled, rounded', fillcolor='#f3e5f5', color='#ab47bc', fontname='Helvetica, Arial, sans-serif', fontsize='16', margin='0.2,0.1')
    c.attr('edge', color='#555555', fontname='Helvetica, Arial, sans-serif', fontsize='14', penwidth='1.5')
    
    # Inputs cluster
    with c.subgraph(name='cluster_Inputs') as ci:
        ci.attr(label='输入数据', style='dashed, rounded', color='#999999', fontname='Helvetica, Arial, sans-serif', fontsize='14', margin='10')
        ci.node('Mode', '候选模式')
        ci.node('Orig', '原始像素')
    
    # Main spine nodes
    c.node('IPD', '1. IPD\n生成预测块', fillcolor='#e1f5fe', color='#0288d1')
    c.node('Sub', '相减', shape='diamond', fillcolor='#ede7f6', color='#7e57c2', margin='0,0')
    c.node('TQ', '2. 变换与量化\n(T/Q)', fillcolor='#fff3e0', color='#f57c00')
    c.node('IQIT', '4. 反量化与\n反变换 (IQ/IT)', fillcolor='#fff3e0', color='#f57c00')
    c.node('Add', '相加', shape='diamond', fillcolor='#ede7f6', color='#7e57c2', margin='0,0')
    c.node('Recon', '5. 生成重建块\n(Recon)', fillcolor='#e8f5e9', color='#2e7d32')
    c.node('Dist', '6. 计算失真 D\n(SAD/SSE)')
    c.node('Cost', '7. 计算 RD Cost\nJ = D + λR', shape='diamond', fillcolor='#fce4ec', color='#c2185b', fontcolor='#880e4f', margin='0,0')
    
    # Branch node
    c.node('Rate', '3. 预估\n比特率 R')

    # 1. Main Backbone (forced straight using weight)
    c.edge('IPD', 'Sub', weight='10')
    c.edge('Sub', 'TQ', weight='10')
    c.edge('TQ', 'IQIT', weight='10')
    c.edge('IQIT', 'Add', weight='10')
    c.edge('Add', 'Recon', weight='10')
    c.edge('Recon', 'Dist', weight='10')
    c.edge('Dist', 'Cost', weight='10')
    
    # 2. Inputs routing
    c.edge('Mode', 'IPD')
    c.edge('Orig', 'Sub', style='dashed')
    c.edge('Orig', 'Dist', style='dashed')
    
    # 3. Rate Branch
    c.edge('TQ', 'Rate', style='dashed')
    c.edge('Rate', 'Cost')
    
    # 4. IPD Forward Branch
    c.edge('IPD', 'Add', style='dashed')

# Render the graph to the assets directory
output_path = os.path.join(os.path.dirname(script_dir), 'assets', 'diagram_8')
dot.render(output_path, cleanup=True)
print(f"Successfully generated {output_path}.svg")
