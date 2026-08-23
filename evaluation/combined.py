from __future__ import annotations


def diagnose(rag_failures: list[str], runtime_result: str) -> str:
    if runtime_result == "INCONCLUSIVE":
        return "RUNTIME_INCONCLUSIVE"
    rag_failed = bool(rag_failures)
    if runtime_result == "PASS" and rag_failed:
        return "RAG_FAILURE"
    if runtime_result == "FAIL" and not rag_failed:
        return "DOC_RUNTIME_MISMATCH"
    if runtime_result == "FAIL" and rag_failed:
        return "NEEDS_REVIEW"
    return "PASS"
