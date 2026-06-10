# Intra Prediction Architecture Design

![Architecture](https://img.shields.io/badge/Hardware-Architecture-3b82f6?style=for-the-badge)
![HEVC/VVC Intra](https://img.shields.io/badge/HEVC%2FVVC-Intra_Prediction-ec4899?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-10b981?style=for-the-badge)

Welcome to the **Intra Prediction Architecture Design** repository. This centralized hub documents the core hardware design philosophies, pipeline optimizations, and algorithmic decoupling mechanisms for the Intra Prediction module.

All documentation is generated and hosted statically via GitHub Pages, delivering an interactive, highly readable, zero-drag "Geek Dashboard" experience.

## 📖 Live Document Links (GitHub Pages)

You can directly access the interactive online documentation via the following link:

### 🎨 1. [Intra Prediction Architecture & MD/RDO Decoupling](https://edgerzou-stack.github.io/intra-pred-architecture/)
- **Target Audience:** Core Intra Architects, Algorithm Engineers, RTL Designers.
- **Content:** A comprehensive analysis of Luma/Chroma decision loops, Rough Mode Decision (MD) vs. Rate-Distortion Optimization (RDO) pipeline decoupling, and advanced hardware bottleneck resolutions.
- **Highlights:**
  - Clear visualizations of Spatial Dependency Bottlenecks.
  - Deep dives into MPM (Most Probable Mode) freeze strategies.
  - Architectural resolutions for extreme small-block (4x4) feedback loops.
  - Native avoidance strategies for CCLM and MRL SRAM bandwidth killers.

## 🛠️ Repository Philosophy

This repository is designed to be **clean and purely web-facing**. We embrace the following principles:
- **Only Track HTML:** We exclusively track `.html` output files in Git to keep the repository extremely clean.
- **Zero Horizontal Scrolling:** All diagrams and tables are designed using a strict 100% relative width or dynamic dimensional sizing rule to ensure 0-drag readability across any display.
- **Hardware UI/UX:** We bring modern Web UI principles (glassmorphism, dark mode, high-contrast alerts) into Hardware Specification viewing.

---
*Maintained by the Core Architecture Team.*
