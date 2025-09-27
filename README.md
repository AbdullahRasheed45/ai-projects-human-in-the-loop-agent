# 🤝 Human-in-the-Loop AI Agent (Agno + Nebius + Interactive Control)

An intelligent AI agent that demonstrates responsible AI interaction by requiring human approval before executing any tool calls. Features fun facts, motivational quotes, and jokes with complete human oversight, retry mechanisms, and dual interface options. Perfect for learning HITL patterns and building trust-based AI systems that keep humans in control.

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Agno](https://img.shields.io/badge/Agno-AI_Framework-green?style=for-the-badge)](https://github.com/agno-ai)
[![Nebius](https://img.shields.io/badge/Nebius-Llama_3-blue?style=for-the-badge)](https://nebius.ai/)
[![Gradio](https://img.shields.io/badge/Gradio-Web_UI-orange?style=for-the-badge)](https://gradio.app/)

✨ **Features**

🛡️ **Human Approval Gate**: Every tool execution requires explicit human consent - no autonomous actions without your permission

🔄 **Smart Retry Mechanism**: Intelligent retry system (up to 3 attempts) allows the agent to refine its approach based on your feedback

🎯 **Three Engaging Tools**: Generate interesting facts, motivational quotes, or entertaining jokes with AI-powered content creation

💻 **Dual Interface Options**: Choose between Rich-styled console interface or intuitive Gradio web UI for different interaction preferences

⚡ **Real-time Control**: Cancel, continue, or retry any action with simple commands, maintaining complete oversight of AI behavior

🧠 **Educational HITL Pattern**: Perfect demonstration of human-in-the-loop architecture for building responsible AI applications

🗂️ **Project structure**
```
.
├─ app.py            # Gradio web interface for browser-based interaction
├─ main.py           # Console runner with Rich-styled human approval flow
├─ .env.example      # Environment template for Nebius API key
├─ requirements.txt  # Python dependencies and package versions
└─ README.md         # Comprehensive documentation
```

🚀 **Quickstart**

**Prerequisites**
- Python 3.8 or higher
- **NEBIUS_API_KEY** (Nebius AI platform access)

**1) Clone & install**
```bash
git clone https://github.com/AbdullahRasheed45/ai-projects-human-in-the-loop-agent.git
cd ai-projects-human-in-the-loop-agent

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add: NEBIUS_API_KEY=your_nebius_api_key_here
```

**2) Run console interface**
```bash
python main.py
```

**Interactive Flow**: The agent will propose actions and wait for your approval before executing any tools:
- **`y`** → Continue (execute the tool)
- **`n`** → Cancel (abort the action)  
- **`retry`** → Try again with refined approach (up to 3 times)

**3) Run web interface**
```bash
python app.py
```

**Browser Experience**: Opens Gradio interface for point-and-click interaction with the same approval controls built into the web UI.

🧠 **How it works (HITL architecture)**

**1. Intent Recognition**: You request content (fact, quote, or joke) through console or web interface

**2. Tool Planning**: Agent analyzes request and selects appropriate content generation tool

**3. **Human Approval Gate**: System pauses and presents the planned action for your explicit approval

**4. **Execution Control**: Based on your response:
   - **Continue** → Tool executes and returns result
   - **Retry** → Agent refines approach and asks again (bounded retries)
   - **Cancel** → Action is aborted, agent adapts or exits gracefully

**5. **Result Delivery**: Approved content is displayed through Rich console formatting or Gradio web interface

⚙️ **Configuration options**

**Model Selection**:
```python
# Default: Nebius Llama-3.3-70B-Instruct
# Switch to other Nebius models for different performance characteristics
MODELS = {
    'fast': 'llama-3-8b-instruct',      # Quicker responses
    'balanced': 'llama-3-70b-instruct', # Standard quality
    'premium': 'llama-3.3-70b-instruct' # Best performance
}
```

**Retry Behavior**:
```python
# Customize retry limits and behavior
MAX_RETRIES = 3                    # Maximum retry attempts
RETRY_DELAY = 1.0                  # Delay between retries (seconds)
PROGRESSIVE_PROMPTING = True       # Refine prompts on each retry
```

**Tool Customization**:
```python
# Extend or modify available tools
tools = {
    'fact_tool': generate_interesting_fact,
    'quote_tool': generate_motivational_quote, 
    'joke_tool': generate_entertaining_joke,
    'custom_tool': your_custom_function      # Add new capabilities
}
```

**Interface Preferences**:
- **Console Mode**: Rich-formatted output with colored text and interactive prompts
- **Web Mode**: Clean Gradio interface with buttons and text areas
- **API Mode**: Programmatic access for integration into larger systems

🧪 **Example interactions**

**Console Interface Flow**:
```bash
> What would you like? (fact | quote | joke)
> joke

🤖 The agent wants to call: joke_tool
💭 Purpose: Generate an entertaining joke for you

Approve this action? [y/n/retry]: y

✅ Joke Generated:
"Why did the developer go broke? Because he used up all his cache!"
```

**Retry Scenario**:
```bash
> What would you like? (fact | quote | joke)  
> quote

🤖 The agent wants to call: quote_tool  
💭 Purpose: Generate a motivational quote

Approve this action? [y/n/retry]: retry

🔄 Retrying (1/3)... Refining approach...
🤖 The agent wants to call: quote_tool
💭 Purpose: Generate an inspiring, personalized motivational quote

Approve this action? [y/n/retry]: y

✅ Quote Generated:
"The only way to do great work is to love what you do." — Steve Jobs
```

**Web Interface Experience**:
- **Input Box**: Enter your request (fact/quote/joke or custom prompt)
- **Approval Dialog**: Interactive approval step with Continue/Retry/Cancel options
- **Output Panel**: Clean display of generated content with formatting
- **History Tracking**: View previous interactions and approvals

🎯 **Content generation examples**

**Interesting Facts**:
- *"Did you know that octopuses have three hearts and blue blood?"*
- *"The Great Wall of China isn't visible from space with the naked eye."*
- *"Honey never spoils - archaeologists have found edible honey in ancient Egyptian tombs."*

**Motivational Quotes**:
- *"Success is not final, failure is not fatal: it is the courage to continue that counts." — Winston Churchill*
- *"The future belongs to those who believe in the beauty of their dreams." — Eleanor Roosevelt*
- *"Innovation distinguishes between a leader and a follower." — Steve Jobs*

**Entertaining Jokes**:
- *"Why do programmers prefer dark mode? Because light attracts bugs!"*
- *"How do you comfort a JavaScript bug? You console it."*
- *"Why did the AI go to therapy? It had too many deep learning issues."*

🛡️ **Why human-in-the-loop matters**

**Trust & Control**: Maintains human agency over AI actions, preventing unexpected or unwanted tool executions

**Learning & Oversight**: Allows users to understand AI decision-making processes before committing to actions

**Risk Mitigation**: Essential pattern for high-stakes applications (emails, purchases, code deployments) where mistakes have consequences

**Iterative Refinement**: Retry mechanism enables collaborative improvement of AI responses through human feedback

**Scalable Pattern**: Same architecture applies to complex enterprise AI systems requiring human approval workflows

**Educational Value**: Perfect introduction to responsible AI development and human-AI collaboration principles

🔧 **Advanced customization**

**Custom Tool Development**:
```python
# Add domain-specific tools
def weather_tool(location: str) -> str:
    """Get weather information with human approval"""
    return f"Weather for {location}: Sunny, 22°C"

def email_tool(recipient: str, message: str) -> str:
    """Send email with human approval (critical for automation)"""
    return f"Email sent to {recipient}: {message}"
```

**Approval Workflow Customization**:
```python
# Customize approval prompts and options
APPROVAL_PROMPTS = {
    'standard': "Approve this action? [y/n/retry]",
    'detailed': "Review and approve:\n{tool_details}\nProceed? [continue/cancel/modify]",
    'risk_aware': "⚠️ This action will {consequences}. Confirm? [yes/no/revise]"
}
```

**Integration Patterns**:
```python
# Embed HITL pattern in larger applications
class HITLWorkflow:
    def __init__(self, approval_handler):
        self.approval_handler = approval_handler
    
    async def execute_with_approval(self, action):
        if await self.approval_handler.request_approval(action):
            return await action.execute()
        return None
```

🔒 **Security & safety considerations**

**API Key Protection**: Store Nebius API keys securely in environment variables, never in code

**Input Validation**: Sanitize user inputs to prevent prompt injection or malicious requests

**Audit Trail**: Log all approval decisions and tool executions for compliance and debugging

**Rate Limiting**: Implement safeguards against excessive API usage or retry loops

**Scope Limitation**: Keep tool capabilities appropriate for the approval level (low-risk for demo, high-oversight for production)

🐛 **Troubleshooting**

**Authentication Issues**:
- **"API Key Missing"** → Verify `NEBIUS_API_KEY` is set in `.env` file and loaded correctly
- **"Invalid API Response"** → Check API key validity and account status at Nebius platform
- **"Rate Limit Error"** → Implement delays between requests or upgrade API plan

**Interaction Problems**:
- **"No Response to Approval"** → Ensure console input is exactly `y`, `n`, or `retry` (case-sensitive)
- **"Tool Not Found"** → Verify tool name matches available options (fact, quote, joke)
- **"Retry Loop"** → Check retry counter and prompt refinement logic

**Interface Issues**:
- **Console Not Displaying** → Install Rich properly: `pip install rich`
- **Gradio Won't Launch** → Run `python app.py` from project root, check port availability
- **Web UI Not Responding** → Clear browser cache, check firewall settings

**Performance & Quality**:
- **Slow Responses** → Switch to faster Nebius model or reduce content complexity
- **Poor Content Quality** → Adjust prompts or upgrade to premium model
- **Too Many Retries** → Reduce max retry limit or improve prompt specificity

☁️ **Deployment strategies**

**Local Development**:
```bash
# Development mode with debug logging
export DEBUG=true
export LOG_LEVEL=debug
python main.py
```

**Web Deployment**:
- **Hugging Face Spaces**: Upload code and set `NEBIUS_API_KEY` in Space secrets
- **Streamlit Cloud**: Deploy Gradio app with environment variable configuration
- **Railway/Render**: Production deployment with proper secret management

**Enterprise Integration**:
```python
# API service wrapper for enterprise systems
from fastapi import FastAPI
from hitl_agent import HITLAgent

app = FastAPI()
agent = HITLAgent()

@app.post("/approve-and-execute")
async def api_with_approval(request: ToolRequest):
    return await agent.execute_with_human_approval(request)
```

**Docker Deployment**:
```dockerfile
FROM python:3.8-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV NEBIUS_API_KEY=""
CMD ["python", "app.py"]
```

🎓 **Learning opportunities**

**AI Safety Concepts**: Understand alignment, control, and human oversight in AI systems

**Agent Architecture**: Learn how to build modular, controllable AI agents with tool integration

**User Experience Design**: Balance AI automation with human agency and control

**Enterprise AI Patterns**: Foundation for building production AI systems with human oversight

**Responsible AI Development**: Implement transparency, accountability, and user control principles

📜 **License**

MIT License - see [LICENSE](LICENSE) file for complete terms. Perfect for educational use, research, and building upon for commercial applications.

## 📞 Connect & Support

<div align="center">

### 🚀 Ready to Build Responsible AI Agents?

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://techvibes360.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abdullahrasheed-/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abdullahrasheed45@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AbdullahRasheed45)

**Let's build AI systems that keep humans in control!**

</div>

---

*Built with ❤️ using responsible AI principles and human-centered design. Perfect for learning HITL patterns and building trustworthy AI applications.*
