from lab.providers import DemoProvider


def test_validate_response_allows_valid_json():
    raw = '{"answer": "Paris is the capital of France.", "confidence": 0.96}'
    payload = __import__('07_llm_application.structured_output', fromlist=['validate_response']).validate_response(raw)
    assert payload["answer"] == "Paris is the capital of France."
    assert payload["confidence"] == 0.96


def test_validate_response_rejects_missing_field():
    raw = '{"answer": "Paris is the capital of France."}'
    try:
        __import__('07_llm_application.structured_output', fromlist=['validate_response']).validate_response(raw)
    except ValueError:
        return
    raise AssertionError("validate_response should reject a missing required field")
