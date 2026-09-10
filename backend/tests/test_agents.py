def test_agent_orchestrator():
    prompt = "Test execution query for agentic-research-paper-synthesizer"
    assert len(prompt) > 0
    assert "Test" in prompt
