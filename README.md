# Retail Intelligence Multi-Agent System
A sophisticated multi-agent workflow built with LangGraph and Google Gemini to perform automated competitive market research. This system simulates a team of specialized retail analysts to help businesses evaluate new store locations

## Overview
This project uses a directed acyclic graph (DAG) to pass a business "state" through five specialized AI agents. Each agent performs a specific task, enriching the data before passing it to the next.

**The Agent Team:**
- **Location Analyst:** Extracts and validates the geographical target from raw user prompts.
- **Competitor Researcher:** Identifies top-tier local and national competitors in the area.
- **Visitor Analyst:** Estimates visitor patterns, comparing weekday vs. weekend dynamics.
- **Strategy Consultant:** Develops actionable business recommendations based on competitor weaknesses.
- **Report Compiler:** Aggregates all findings into a professional, executive-ready Markdown report.
---

## Tech Stack
- **Orchestration:** LangGraph
- **LLM:** Google Gemini 2.5-flash-lite (via langchain-google-genai)
- **Language:** Python 3.12+
- **State Management:** Python TypedDict

---
## Getting Started

**1. Prerequisites**
- Ensure you have a Google Gemini API Key. You can get one at Google AI Studio

**2. Installation**
```
pip install -U langgraph langchain-google-genai google-genai
```
**3. Usage**
```
from langgraph.graph import StateGraph, END
# ... (see main script for full implementation)

# Define your business idea
input_state = {
    "input_prompt": "I want to open a new clothing retail store in downtown San Francisco"
}

# Execute the graph
result = app.invoke(input_state)
print(result["report"])
```
**4. Example Output**
**The system generates a detailed Competitive Intelligence Report including:
Competitor Snapshots:** (e.g., Nordstrom, Macy's, H&M, Zara, Uniqlo)
**Traffic Drivers:** Analysis of office workers vs. weekend tourists.
**Strategic Pillars:** Recommendations for "Click & Collect" optimization, "San Francisco Style" curated collections, and "Power Hour" weekday promotions.

```
    Competitive Intelligence Report for Retail Business

    Location: Downtown San Francisco
    Competitors: Nordstrom, Macy's, H&M, Zara, Uniqlo
    Visitors: ## Downtown San Francisco Retail Foot Traffic Analysis: Competitor Snapshot

**Executive Summary:**

This analysis estimates the foot traffic for key retailers in Downtown San Francisco, considering store size, location, and general brand appeal. Nordstrom and Macy's, as anchor department stores, are expected to draw the highest overall traffic, particularly on weekends. Fast fashion retailers like H&M, Zara, and Uniqlo will see significant weekday traffic driven by local workers and shoppers, with a notable surge on weekends due to their appeal to a broader demographic.

**Competitor Foot Traffic Estimates (Downtown San Francisco):**

*   **Nordstrom:**
    *   **Estimated Visitors:** High
    *   **Key Drivers:** Established brand reputation, broad product offering (apparel, accessories, cosmetics), prime location, and strong weekend draw.
    *   **Weekday vs. Weekend:** Weekends will see a significant increase in traffic compared to weekdays, driven by leisure shoppers and tourists.

*   **Macy's:**
    *   **Estimated Visitors:** High
    *   **Key Drivers:** Large store footprint, diverse merchandise categories, strong brand recognition, and a central location.
    *   **Weekday vs. Weekend:** Similar to Nordstrom, Macy's experiences a substantial uplift in foot traffic on weekends. Weekdays benefit from local office workers and targeted shoppers.

*   **H&M:**
    *   **Estimated Visitors:** Moderate to High
    *   **Key Drivers:** Trendy and affordable fashion, accessible price points, and a strong appeal to younger demographics and budget-conscious shoppers.
    *   **Weekday vs. Weekend:** Weekdays will see consistent traffic from office workers and students. Weekends will experience a notable surge as it becomes a destination for fashion-forward browsing and purchasing.

*   **Zara:**
    *   **Estimated Visitors:** Moderate to High
    *   **Key Drivers:** Fashion-forward and on-trend apparel, perceived higher quality than some fast fashion competitors, and a strong brand image.
    *   **Weekday vs. Weekend:** Weekdays will attract shoppers seeking current styles for work and social occasions. Weekends will see a significant increase in traffic, driven by its popularity for trend-driven purchases.

*   **Uniqlo:**
    *   **Estimated Visitors:** Moderate to High
    *   **Key Drivers:** Focus on functional, high-quality basics and innovative materials, appealing to a wide demographic seeking value and practicality.
    *   **Weekday vs. Weekend:** Weekdays will benefit from local shoppers and those seeking everyday essentials. Weekends will see a strong increase as it attracts a broader audience looking for versatile and affordable clothing.

**Key Considerations:**

*   **Location Attractiveness:** All listed competitors benefit from prime downtown San Francisco locations, situated within high-traffic retail corridors and near public transportation hubs.
*   **Store Size:** Nordstrom and Macy's, as department stores, have a significant advantage in drawing and accommodating larger volumes of shoppers due to their extensive floor space.
*   **Weekday vs. Weekend Dynamics:** Weekends are consistently the peak traffic periods for all retailers, driven by leisure shopping. Weekdays are influenced by the presence of office workers, tourists, and targeted shoppers.
*   **Brand Appeal:** Each brand has a distinct appeal, attracting different customer segments. Nordstrom and Macy's cater to a broader, more established shopper base, while H&M, Zara, and Uniqlo resonate strongly with trend-conscious and value-seeking consumers.

**Recommendations:**

*   **Staffing & Inventory:** Ensure adequate staffing and inventory levels, particularly on weekends, to manage peak traffic and maximize sales opportunities.
*   **Promotional Strategies:** Tailor promotional activities to weekday and weekend traffic patterns. Consider weekday promotions to drive traffic during slower periods and weekend events to capitalize on higher footfall.
*   **Customer Experience:** Focus on delivering a positive in-store experience to encourage repeat visits and positive word-of-mouth, especially for the fast fashion retailers.      
    Strategy: ## Retail Strategy Recommendations: Downtown San Francisco

**Objective:** To attract more visitors and differentiate from competitors in Downtown San Francisco.

**Analysis Summary:**

*   **Anchor Stores (Nordstrom, Macy's):** High overall traffic, especially weekends. Broad appeal, large footprint.
*   **Fast Fashion (H&M, Zara, Uniqlo):** Moderate to High traffic, significant weekday draw from office workers, strong weekend surge. Appeal to younger, trend-conscious, and value-seeking demographics.
*   **Common Strengths:** Prime locations, proximity to transit.
*   **Key Differentiator:** Brand appeal and target customer segments.

**Actionable Recommendations:**

**1. Enhance In-Store Experience & Differentiation:**

*   **Curated Collections & Experiential Zones:**
    *   **Action:** Create distinct "zones" within the store that highlight specific trends, occasions (e.g., "Work from Anywhere Essentials," "Weekend Getaway Style"), or collaborations.
    *   **Benefit:** Offers a more engaging and personalized shopping journey, differentiating from the broader offerings of department stores and the more uniform feel of some fast fashion.
*   **"San Francisco Style" Focus:**
    *   **Action:** Feature a curated selection of items that reflect the unique style and needs of San Francisco residents (e.g., versatile pieces for changing weather, sustainable fashion options, local designer collaborations).
    *   **Benefit:** Creates a strong local connection and a unique selling proposition that competitors may not emphasize.
*   **Interactive Elements & Technology:**
    *   **Action:** Implement interactive fitting rooms with styling suggestions, digital lookbooks, or a "style quiz" to personalize recommendations.
    *   **Benefit:** Enhances engagement, provides value-added services, and captures customer data for future personalization.

**2. Targeted Pricing & Promotion Strategies:**

*   **Weekday "Power Hours" Promotions:**
    *   **Action:** Offer exclusive discounts or "buy one, get one" deals during specific weekday hours (e.g., 11 AM - 2 PM) targeting office workers.
    *   **Benefit:** Drives traffic during slower periods and captures impulse purchases from the weekday commuter base.
*   **Weekend "Discovery" Events:**
    *   **Action:** Host small, engaging events on weekends like styling workshops, new collection previews with local influencers, or "meet the designer" sessions.
    *   **Benefit:** Creates a destination experience, encourages longer stays, and generates social media buzz.
*   **Loyalty Program with Experiential Rewards:**
    *   **Action:** Beyond discounts, offer rewards like early access to sales, invitations to exclusive events, or personalized styling consultations for loyal customers.
    *   **Benefit:** Fosters customer loyalty and encourages repeat visits by offering unique value.

**3. Optimize Store Layout & Merchandising:**

*   **"Hero" Product Placement:**
    *   **Action:** Strategically place high-demand, trend-setting items at the front of the store or in high-visibility areas to immediately capture attention.
    *   **Benefit:** Drives immediate interest and encourages exploration of the store.
*   **Cross-Merchandising for Outfit Building:**
    *   **Action:** Group complementary items together (e.g., tops with matching bottoms, accessories with outfits) to inspire complete looks and increase average transaction value.  
    *   **Benefit:** Simplifies the shopping process for customers and encourages them to purchase more.
*   **Dynamic Visual Merchandising:**
    *   **Action:** Regularly update window displays and in-store mannequins to reflect current trends and seasonal themes, creating a sense of freshness and urgency.
    *   **Benefit:** Attracts attention from passersby and keeps the store looking current and exciting.

**4. Leverage Digital & Omnichannel Integration:**

*   **"Click & Collect" Optimization:**
    *   **Action:** Ensure a seamless and efficient "buy online, pick up in-store" (BOPIS) experience with dedicated pick-up points and clear signage.
**4. Leverage Digital & Omnichannel Integration:**

*   **"Click & Collect" Optimization:**
    *   **Action:** Ensure a seamless and efficient "buy online, pick up in-store" (BOPIS) experience with dedicated pick-up points and clear signage.
    *   **Benefit:** Caters to the convenience-seeking shopper and drives in-store traffic for order fulfillment.
*   **Social Media Engagement & Geo-Targeted Ads:**
    *   **Action:** Utilize social media to showcase new arrivals, promote events, and run geo-targeted advertising campaigns to reach potential customers in the immediate vicinity.  
    *   **Benefit:** Increases brand awareness and drives targeted foot traffic.

**4. Leverage Digital & Omnichannel Integration:**

*   **"Click & Collect" Optimization:**
    *   **Action:** Ensure a seamless and efficient "buy online, pick up in-store" (BOPIS) experience with dedicated pick-up points and clear signage.
    *   **Benefit:** Caters to the convenience-seeking shopper and drives in-store traffic for order fulfillment.
*   **Social Media Engagement & Geo-Targeted Ads:**
    *   **Action:** Utilize social media to showcase new arrivals, promote events, and run geo-targeted advertising campaigns to reach potential customers in the immediate vicinity.  
    *   **Benefit:** Increases brand awareness and drives targeted foot traffic.
**4. Leverage Digital & Omnichannel Integration:**

*   **"Click & Collect" Optimization:**
    *   **Action:** Ensure a seamless and efficient "buy online, pick up in-store" (BOPIS) experience with dedicated pick-up points and clear signage.
    *   **Benefit:** Caters to the convenience-seeking shopper and drives in-store traffic for order fulfillment.

*   **"Click & Collect" Optimization:**
    *   **Action:** Ensure a seamless and efficient "buy online, pick up in-store" (BOPIS) experience with dedicated pick-up points and clear signage.
*   **"Click & Collect" Optimization:**
    *   **Action:** Ensure a seamless and efficient "buy online, pick up in-store" (BOPIS) experience with dedicated pick-up points and clear signage.
    *   **Benefit:** Caters to the convenience-seeking shopper and drives in-store traffic for order fulfillment.
    *   **Action:** Ensure a seamless and efficient "buy online, pick up in-store" (BOPIS) experience with dedicated pick-up points and clear signage.
    *   **Benefit:** Caters to the convenience-seeking shopper and drives in-store traffic for order fulfillment.
    *   **Benefit:** Caters to the convenience-seeking shopper and drives in-store traffic for order fulfillment.
*   **Social Media Engagement & Geo-Targeted Ads:**
    *   **Action:** Utilize social media to showcase new arrivals, promote events, and run geo-targeted advertising campaigns to reach potential customers in the immediate vicinity.  
    *   **Benefit:** Increases brand awareness and drives targeted foot traffic.

By implementing these recommendations, the retail business can effectively attract more visitors, create a distinct competitive advantage, and foster stronger customer loyalty in the dynamic Downtown San Francisco market.
```

## License

MIT License
