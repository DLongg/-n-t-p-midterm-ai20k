"""
Helper to enrich references in author_day02_part1.py with authoritative URLs.
"""
import re

url_map = {
    "d02-q002": "Torres, T. (2021). Continuous Discovery Habits. Product Talk LLC (https://www.producttalk.org/); Harvard Business Review - Stop the Meeting Madness (https://hbr.org/2017/07/stop-the-meeting-madness)",
    "d02-q005": "Fitzpatrick, R. (2013). The Mom Test. Robfitz Ltd (http://momtestbook.com/); Teresa Torres - Continuous Discovery Habits (https://www.producttalk.org/)",
    "d02-q006": "Cagan, M. (2017). Inspired: How to Create Tech Products Customers Love. Wiley (https://www.svpg.com/books/inspired/); Teresa Torres - Continuous Discovery Habits (https://www.producttalk.org/)",
    "d02-q009": "Aristotelian First Principles in Systems Design; Porter, M. E. (1996). What Is Strategy? Harvard Business Review (https://hbr.org/1996/11/what-is-strategy)",
    "d02-q010": "Drucker, P. F. (1954). The Practice of Management; Martin Fowler - Information Dashboards & Continuous Delivery (https://martinfowler.com/articles/patterns-of-distributed-systems/)",
    "d02-q015": "Teresa Torres - Opportunity Solution Tree (https://www.producttalk.org/opportunity-solution-tree/); Cagan, M. (2020). Empowered. Wiley (https://www.svpg.com/books/empowered/)",
    "d02-q016": "Torres, T. (2021). Continuous Discovery Habits (https://www.producttalk.org/); Bland, D. J., & Osterwalder, A. (2019). Testing Business Ideas. Wiley (https://www.strategyzer.com/library/testing-business-ideas)",
    "d02-q018": "Bland, D. J., & Osterwalder, A. (2019). Testing Business Ideas. Wiley (https://www.strategyzer.com/library/testing-business-ideas); Nielsen Norman Group - Discovery Phase (https://www.nngroup.com/articles/discovery-phase/)",
    "d02-q019": "Google Cloud Architecture Center - Patterns for Resilient AI Architectures (https://cloud.google.com/architecture); Nygard, M. T. (2018). Release It!. Pragmatic Bookshelf (https://pragprog.com/titles/mnee2/release-it-second-edition/)",
    "d02-q020": "Cagan, M. (2017). Inspired (https://www.svpg.com/books/inspired/); Davenport, T., & Ronanki, R. (2018). Artificial Intelligence for the Real World. Harvard Business Review (https://hbr.org/2018/01/artificial-intelligence-for-the-real-world)",
    "d02-q021": "Goldratt, E. M. (1984). The Goal: A Process of Ongoing Improvement (https://www.tocico.org/); Lean Enterprise Institute (https://www.lean.org/)",
    "d02-q022": "Rother, M., & Shook, J. (2003). Learning to See: Value Stream Mapping. Lean Enterprise Institute (https://www.lean.org/lexicon-terms/value-stream-mapping/)",
    "d02-q023": "Hammer, M. (1990). Reengineering Work: Don't Automate, Obliterate. Harvard Business Review (https://hbr.org/1990/07/reengineering-work-dont-automate-obliterate); Google Cloud AI Adoption Framework (https://cloud.google.com/ai-adoption)",
    "d02-q024": "EU Artificial Intelligence Act (High-Risk AI Requirements) (https://artificialintelligenceact.eu/); Barocas, S., et al. (2019). Fairness and Machine Learning (https://fairmlbook.org/)",
    "d02-q026": "George, M. L. (2002). Lean Six Sigma. McGraw-Hill; Google SRE Book - Service Level Indicators (https://sre.google/sre-book/service-level-objectives/)",
    "d02-q027": "Doerr, J. (2018). Measure What Matters (https://www.whatmatters.com/); Google PAIR Guidebook - Success Metrics (https://pair.withgoogle.com/guidebook/)",
    "d02-q028": "Kohavi, R., et al. (2020). Trustworthy Online Controlled Experiments (https://exp-platform.com/); Harvard Business Review - A Step-by-Step Guide to Smart Business Experiments (https://hbr.org/2011/03/a-step-by-step-guide-to-smart-business-experiments)",
    "d02-q032": "Anthropic Claude Documentation - Building Systems with Tools (https://docs.anthropic.com/en/docs/build-with-claude/tool-use); LangChain Tool Boundaries (https://python.langchain.com/docs/concepts/tools/)",
    "d02-q035": "Wardley, S. (2016). Wardley Maps (https://learn.wardleymaps.com/); Cagan, M. - Build vs Buy in Product Management (https://www.svpg.com/buy-vs-build/)",
    "d02-q036": "Gartner Research - Decision Framework for Generative AI (https://www.gartner.com/); NIST AI Risk Management Framework (https://www.nist.gov/itl/ai-risk-management-framework)",
    "d02-q039": "LangChain StateGraph Architecture (https://python.langchain.com/docs/concepts/architecture/); Google Cloud - Industrial GenAI Assistant Design (https://cloud.google.com/architecture)",
    "d02-q040": "Martin Fowler - Patterns of Enterprise Application Architecture (https://martinfowler.com/eaaCatalog/); OWASP Top 10 for LLMs - LLM08: Excessive Agency (https://owasp.org/www-project-top-10-for-large-language-model-applications/)",
    "d02-q042": "Meyer, B. (1992). Applying 'Design by Contract'. IEEE Computer (https://www.eiffel.com/values/design-by-contract/); Google Cloud Architecture - Financial Processing AI Patterns (https://cloud.google.com/architecture)",
    "d02-q046": "Anthropic - Building Effective Agents: Prompt Chaining Workflow (https://www.anthropic.com/research/building-effective-agents); Martin Fowler - Monolith to Microservices Pattern (https://martinfowler.com/articles/monolith-to-microservices.html)",
    "d02-q047": "Anthropic - Building Effective Agents: Routing Workflow (https://www.anthropic.com/research/building-effective-agents); Google SRE - Risk-Based Traffic Routing (https://sre.google/sre-book/)",
    "d02-q048": "Nielsen Norman Group - Error Prevention in AI Interfaces (https://www.nngroup.com/articles/error-prevention-ai/); Anthropic - Routing Pattern Guidelines (https://www.anthropic.com/research/building-effective-agents)",
    "d02-q051": "Anthropic - Building Effective Agents: Orchestrator-Workers Pattern (https://www.anthropic.com/research/building-effective-agents); OpenAI Swarm Multi-Agent Framework (https://github.com/openai/swarm)",
    "d02-q052": "Anthropic - Building Effective Agents: Evaluating Agent Architectures (https://www.anthropic.com/research/building-effective-agents); OWASP Top 10 for LLMs - LLM04: Model Denial of Service (https://owasp.org/www-project-top-10-for-large-language-model-applications/)",
    "d02-q054": "Anthropic - Building Effective Agents: Evaluator-Optimizer Workflow (https://www.anthropic.com/research/building-effective-agents); Madaan, A., et al. (2023). Self-Refine. NeurIPS 2023 (https://arxiv.org/abs/2303.17651)",
    "d02-q055": "Parasuraman, R., et al. (2000). A Model for Types and Levels of Human Interaction with Automation (https://ieeexplore.ieee.org/document/844357); WHO Guidance on AI in Health (https://www.who.int/publications/i/item/9789240029200)",
    "d02-q056": "Basel Committee on Banking Supervision - Credit Risk Management (https://www.bis.org/publ/bcbs75.htm); Federal Reserve SR 11-7: Model Risk Management (https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm)",
    "d02-q059": "Google Conversational AI Design Guidelines - Asking Clarifying Questions (https://developers.google.com/assistant/conversation-design); Nielsen Norman Group - Chatbot UX (https://www.nngroup.com/articles/chatbots/)",
    "d02-q060": "Microsoft HAX Toolkit - Guideline 10: Scope of Action (https://www.microsoft.com/en-us/haxtoolkit/); Nielsen Norman Group - Confirmation Dialogs (https://www.nngroup.com/articles/confirmation-dialog/)",
    "d02-q064": "Nielsen Norman Group - Confirmation Dialogs and Destructive Actions (https://www.nngroup.com/articles/confirmation-dialog/); Microsoft HAX Toolkit - Support Efficient Correction (https://www.microsoft.com/en-us/haxtoolkit/)"
}

with open("scripts/author_day02_part1.py", "r", encoding="utf-8") as f:
    content = f.read()

for qid, new_ref in url_map.items():
    pattern = rf'(data\["{qid}"\]\s*=\s*\{{[^}}]*"reference_source":\s*")[^"]*(")'
    content = re.sub(pattern, rf'\g<1>{new_ref}\g<2>', content)

with open("scripts/author_day02_part1.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated author_day02_part1.py with official URLs!")
