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

## Tech Stack
- **Orchestration:** LangGraph
- **LLM:** Google Gemini 2.5-flash-lite (via langchain-google-genai)
- **Language:** Python 3.12+
- **State Management:** Python TypedDict

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
**The system generates a detailed Competitive Intelligence Report including:**
- **Competitor Snapshots:** (e.g., Nordstrom, Macy's, H&M, Zara, Uniqlo)
- **Traffic Drivers:** Analysis of office workers vs. weekend tourists.
- **Strategic Pillars:** Recommendations for "Click & Collect" optimization, "San Francisco Style" curated collections, and "Power Hour" weekday promotions.

**Competitive Intelligence Report for Retail Business :**

- **Location:** downtown San Francisco
- **Competitors:** Macy's, Nordstrom, H&M, Zara, Uniqlo
- **Visitors:** Here's an analysis of retail foot traffic for downtown San Francisco competitors:

**Downtown San Francisco Retail Foot Traffic Analysis**

The downtown San Francisco retail landscape, particularly around Union Square and Powell Street, benefits from significant tourist traffic, local shoppers, and office workers. Foot traffic patterns show a clear distinction between weekdays, driven by a mix of local activity and early tourists, and weekends, which see a substantial surge from leisure shoppers and a higher volume of tourists.

---

**Competitor Foot Traffic Estimates:**

*   **Nordstrom (Note: Downtown SF location closed in August 2023)**
    *   *For the purpose of this analysis, assuming a prime downtown location were still operational:*
    *   **Estimated Daily Visitors:**
        *   **Weekdays:** 2, 500 - 3, 800
        *   **Weekends:** 4, 000 - 6, 000
    *   **Insights:** Nordstrom historically attracted a premium demographic with a focus on quality and service. Its large store size and prime location within the SF Centre (when operational) ensured consistent, albeit perhaps less impulse-driven, foot traffic. Weekends would have seen a notable increase from leisure shoppers.

*   **Macy's (Union Square Flagship)**
    *   **Estimated Daily Visitors:**
        *   **Weekdays:** 3, 000 - 4, 500
        *   **Weekends:** 5, 000 - 7, 500
    *   **Insights:** As an iconic, multi-story flagship store on Union Square, Macy's benefits from immense brand recognition and a highly attractive location. It serves a broad demographic, from tourists seeking souvenirs to locals shopping for department store staples. Its sheer size allows for high visitor capacity, with weekends experiencing a significant boost from leisure and tourist traffic.

*   **Zara (Stockton Street)**
    *   **Estimated Daily Visitors:**
        *   **Weekdays:** 3, 800 - 5, 500
        *   **Weekends:** 6, 000 - 8, 500
    *   **Insights:** Zara's prominent Stockton Street location, coupled with its fast-fashion model and strong brand appeal, drives very high foot traffic. It attracts a fashion-conscious demographic looking for trendy, affordable apparel. The store's layout encourages browsing and quick purchases, leading to high visitor turnover, especially on weekends when leisure shopping peaks.

*   **Uniqlo (Powell Street)**
    *   **Estimated Daily Visitors:**
        *   **Weekdays:** 4, 000 - 6, 000
        *   **Weekends:** 6, 500 - 9, 000
    *   **Insights:** Situated on the bustling Powell Street, Uniqlo benefits from extremely high pedestrian traffic, including a significant tourist presence near the cable car turnaround. Its focus on quality basics and functional apparel appeals to a wide demographic. The large, accessible store design facilitates high visitor volume, with weekends seeing a substantial surge from both tourists and local shoppers seeking everyday essentials.

*   **H&M (Powell Street)**
    *   **Estimated Daily Visitors:**
        *   **Weekdays:** 4, 500 - 6, 500
        *   **Weekends:** 7, 000 - 10, 000+
    *   **Insights:** H&M's prime location on Powell Street, directly in a high-traffic tourist corridor, positions it for the highest raw foot traffic among these competitors. Its fast-fashion, high-turnover model, combined with attractive pricing, draws a very large and diverse crowd, particularly younger demographics and impulse buyers. Weekends are exceptionally busy, driven by peak tourist activity and leisure shopping.

---

**Key Takeaways:**

*   **Location is Paramount:** Retailers on Powell Street (H&M, Uniqlo) leverage direct exposure to massive pedestrian and tourist flows, resulting in the highest visitor counts.     
*   **Fast Fashion Dominance:** H&M and Zara's fast-fashion models drive high visitor turnover and impulse purchases, contributing to their strong foot traffic.
*   **Weekend Surge:** All retailers experience a significant increase in visitors on weekends (typically 40-70% higher than weekdays), primarily due to increased leisure shopping and tourist activity.
*   **Flagship Appeal:** Macy's, despite its traditional department store model, maintains strong visitor numbers due to its iconic status and broad appeal as a destination.
    Strategy: **Competitive Strategy for Downtown San Francisco Retail**

**I. Executive Summary & Key Insights**

The downtown San Francisco retail landscape is highly competitive, driven by significant tourist, local shopper, and office worker traffic. Key insights from competitor foot traffic analysis reveal:

*   **Location Dominance:** Retailers on Powell Street (H&M, Uniqlo) leverage direct exposure to massive pedestrian and tourist flows, resulting in the highest visitor counts.        
*   **Fast Fashion & Basics Appeal:** H&M, Zara, and Uniqlo's models (fast fashion, trendy, affordable, or quality basics) drive high visitor turnover and impulse purchases.
*   **Weekend Surge:** All retailers experience a substantial increase in visitors on weekends (40-70% higher than weekdays), primarily due to increased leisure shopping and tourist activity.
*   **Flagship Destination:** Macy's maintains strong visitor numbers due to its iconic status and broad appeal as a destination.

To compete effectively, our strategy must focus on differentiation, leveraging peak traffic periods, and optimizing the in-store experience.

**II. Strategic Imperatives**

1.  **Cultivate a Distinctive Brand Identity:** Differentiate beyond price to create a compelling reason for visitors to choose us over established giants.
2.  **Maximize Weekend & Tourist Engagement:** Capitalize on peak traffic periods and the high volume of leisure shoppers and tourists.
3.  **Optimize In-Store Experience:** Transform the physical space into an engaging and memorable destination.

**III. Actionable Recommendations**

**A. Attracting Visitors & Driving Foot Traffic**

*   **Hyper-Local Partnerships:** Collaborate with local hotels, tour operators, and convention centers to offer exclusive discounts or co-promotions, directly targeting the high volume of tourists.
*   **Experiential Events:** Host regular in-store events (e.g., local artisan pop-ups, styling workshops, product launches, community gatherings) to create buzz and a reason to visit beyond transactional shopping.
*   **Dynamic Window Displays:** Invest in highly engaging, frequently updated window displays that tell a story or showcase unique products, designed to capture attention from high foot traffic, especially on weekends.
*   **Digital Visibility:** Ensure strong local SEO and geo-targeted social media campaigns to appear prominently in "things to do/shop in SF" searches and attract nearby visitors.   

**B. Differentiation & Value Proposition**

*   **Curated Product Assortment:** Focus on a unique, niche product selection that isn't readily available at mass-market competitors (e.g., sustainable fashion, local designer collaborations, artisanal goods, tech-integrated apparel).
*   **Exceptional Service Model:** Implement a highly personalized customer service approach, offering expert advice, concierge-like services, or unique in-store experiences that elevate the shopping journey above transactional fast fashion.
*   **Brand Storytelling:** Clearly communicate our brand's unique story, values (e.g., sustainability, craftsmanship, community support), and the "why" behind our products to resonate with conscious consumers and create emotional connections.

**C. Store Layout & Customer Experience**

*   **Immersive Store Design:** Create an inviting and memorable physical space with unique aesthetics, comfortable lounge areas, interactive displays, and "Instagrammable" moments that encourage exploration and dwell time.
*   **Intuitive Navigation:** Design a clear, easy-to-navigate layout that encourages discovery while minimizing friction, especially during peak weekend traffic. Optimize product adjacencies to inspire cross-category purchases.
*   **Seamless Checkout:** Implement efficient checkout processes (e.g., mobile POS, self-checkout options, multiple stations) to reduce wait times and improve overall satisfaction, particularly during busy periods.
*   **Sensory Branding:** Utilize distinct music, scent, and lighting to create a unique and pleasant atmosphere that reinforces the brand identity and enhances the overall customer experience.

**D. Pricing & Promotions**

*   **Value-Based Pricing:** Position products based on their unique value, quality, and story, rather than solely competing on price with fast-fashion giants. Justify pricing through superior materials, craftsmanship, or exclusivity.
*   **Targeted Promotions:**
    *   **Weekend Specials:** Offer exclusive promotions, bundles, or limited-time offers specifically designed to capitalize on the weekend leisure shopper and tourist surge.        
    *   **Local Loyalty Program:** Implement a tiered loyalty program for local residents and office workers, offering exclusive discounts, early access to new collections, or personalized rewards.
    *   **Tourist Incentives:** Consider small, value-add incentives for tourists (e.g., a unique SF-themed gift with purchase over a certain amount, or a discount with a hotel key card).
*   **Dynamic Bundling:** Create attractive product bundles that offer perceived value and encourage higher average transaction values, especially for complementary items.

## License

MIT License
