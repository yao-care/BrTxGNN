---
layout: default
title: SMART on FHIR
nav_order: 2
has_children: true
description: BrTxGNN SMART on FHIR Application - Query drug repurposing candidates from EHR medication data
permalink: /smart/
---

# SMART on FHIR Application

BrTxGNN provides SMART on FHIR integration, allowing healthcare institutions to read patient medication data from electronic health record (EHR) systems and automatically query related drug repurposing candidates.

---

## What is SMART on FHIR?

SMART on FHIR is an open standard that allows healthcare applications to securely access data in electronic health record systems. Through this standard:

- Applications can obtain authorization from EHR systems
- Read patient medication records, diagnoses, and other data
- Seamlessly integrate into EHR workflows

---

## Features

| Feature | Description |
|---------|-------------|
| **Patient Medication Retrieval** | Automatically retrieve the patient's current medication list from EHR |
| **Drug Mapping** | Map RxNorm drug codes to BrTxGNN database |
| **Repurposing Query** | Display predicted new indication candidates for each drug |
| **Evidence Level Marking** | Clearly mark the evidence level for each prediction (L1-L5) |
| **Clinical Trials Query** | Real-time query of related clinical trials on ClinicalTrials.gov |
| **Drug-Drug Interactions** | Automatically check DDI and display warnings |

---

## Quick Start

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
  <div style="padding: 1.5rem; background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); border-radius: 12px; border: 2px solid #4caf50;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🎯</div>
    <strong style="font-size: 1.1rem; color: #2e7d32;">Standalone Test Mode</strong>
    <p style="color: #555; margin: 0.5rem 0 1rem;">No EHR connection needed. Enter drug names directly to test functionality</p>
    <a href="standalone.html" style="display: inline-block; padding: 8px 16px; background: #4caf50; color: white; text-decoration: none; border-radius: 6px; font-size: 0.9rem;">Try Now &rarr;</a>
  </div>
  <div style="padding: 1.5rem; background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); border-radius: 12px; border: 2px solid #2196f3;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">📖</div>
    <strong style="font-size: 1.1rem; color: #1565c0;">User Guide</strong>
    <p style="color: #555; margin: 0.5rem 0 1rem;">Step-by-step tutorial: How to use BrTxGNN SMART App</p>
    <a href="guide/" style="display: inline-block; padding: 8px 16px; background: #2196f3; color: white; text-decoration: none; border-radius: 6px; font-size: 0.9rem;">View Guide &rarr;</a>
  </div>
  <div style="padding: 1.5rem; background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); border-radius: 12px; border: 2px solid #ff9800;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚙️</div>
    <strong style="font-size: 1.1rem; color: #e65100;">Technical Docs</strong>
    <p style="color: #555; margin: 0.5rem 0 1rem;">OAuth configuration, FHIR API, drug mapping workflow</p>
    <a href="technical-docs/" style="display: inline-block; padding: 8px 16px; background: #ff9800; color: white; text-decoration: none; border-radius: 6px; font-size: 0.9rem;">Technical Specs &rarr;</a>
  </div>
  <div style="padding: 1.5rem; background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%); border-radius: 12px; border: 2px solid #9c27b0;">
    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔗</div>
    <strong style="font-size: 1.1rem; color: #7b1fa2;">Integrations</strong>
    <p style="color: #555; margin: 0.5rem 0 1rem;">ClinicalTrials.gov, DDI checking, CDS Hooks</p>
    <a href="integrations/" style="display: inline-block; padding: 8px 16px; background: #9c27b0; color: white; text-decoration: none; border-radius: 6px; font-size: 0.9rem;">View Integrations &rarr;</a>
  </div>
</div>

---

## Listed on SMART App Gallery

<div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); border-radius: 12px; padding: 1.5rem; margin: 1.5rem 0; border: 2px solid #4caf50;">
  <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
    <img src="{{ '/assets/images/smart-app-icon.png' | relative_url }}" alt="BrTxGNN App Icon" style="width: 64px; height: 64px; border-radius: 12px;">
    <div>
      <div style="font-weight: 600; font-size: 1.2rem; color: #2e7d32;">brtxgnn-smart-app</div>
      <div style="color: #555;">Yao.Care Technology Co., Ltd.</div>
    </div>
  </div>
  <p style="margin-bottom: 1rem; color: #333;">Query drug repurposing candidates for patient medications using TxGNN knowledge graph predictions.</p>
  <a href="https://apps.smarthealthit.org/app/brtxgnn-smart-app" target="_blank" style="display: inline-block; padding: 10px 20px; background: #333; color: white; text-decoration: none; border-radius: 8px; font-weight: 500;">View on SMART App Gallery ↗</a>
</div>

---

## Documentation Structure

| Page | Description |
|------|-------------|
| [User Guide](guide/) | Step-by-step tutorial for general users |
| [Technical Docs](technical-docs/) | FHIR configuration, API endpoints for developers |
| [Integrations](integrations/) | External resource integrations and links |

---

## Disclaimer

<div style="background: #fff3cd; border: 1px solid #ffc107; border-radius: 8px; padding: 16px; margin: 20px 0;">
<strong>Important Notice</strong><br>
The content of this website is provided for research purposes only and does not replace professional medical advice. All drug repurposing prediction results need to be clinically validated before application. If you have health concerns, please consult a qualified healthcare professional.
</div>
