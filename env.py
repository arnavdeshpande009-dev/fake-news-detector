class FakeNewsEnv:

    def __init__(self):
        self.text = ""

    def reset(self):
        self.text = ""
        return self.state()

    def state(self):
        return {"text": self.text}

    def step(self, action):

        # 🔒 EMPTY INPUT
        if not self.text.strip():
            return {
                "observation": {
                    "prediction": "real news",
                    "confidence": 0.5,
                    "reason": "Empty input"
                },
                "reward": 0.0,
                "done": True,
                "info": {"ai_prediction": "real news"}
            }

        # 🔒 LIMIT LENGTH
        if len(self.text) > 1000:
            self.text = self.text[:1000]

        text = self.text.lower()

        # 🔥 KEYWORD RULES (UPGRADED)
        suspicious_words = [
            "fake", "viral", "shocking", "breaking",
            "whatsapp", "forwarded", "aliens", "exposed",

            # NEW STRONG SIGNALS
            "cure", "instantly", "overnight", "miracle",
            "secret", "revealed", "experts shocked",
            "doctors hate", "government secretly",
            "100%", "guaranteed", "unknown truth"
        ]

        rule_fake = any(word in text for word in suspicious_words)

        # 🔥 STRONG PATTERN DETECTION (NEW)
        strong_fake_patterns = [
            "cures all",
            "100% cure",
            "instant cure",
            "overnight cure",
            "doctors hate",
            "miracle cure",
            "secret plan",
            "government secretly",
            "experts shocked"
        ]

        pattern_fake = any(p in text for p in strong_fake_patterns)

        # 🔥 SOURCE CHECK
        trusted_sources = ["bbc", "reuters", "ndtv", "the hindu", "toi"]
        untrusted_sources = ["whatsapp", "forwarded", "telegram", "viral"]

        source_score = 0
        if any(src in text for src in trusted_sources):
            source_score += 1
        if any(src in text for src in untrusted_sources):
            source_score -= 1

        # 🔥 SIMPLE AI SIGNAL
        if "fake" in text or "viral" in text:
            ai_label = "fake news"
        elif "misleading" in text:
            ai_label = "misleading"
        else:
            ai_label = "real news"

        # 🔥 FINAL DECISION (UPDATED)
        if rule_fake or pattern_fake or source_score < 0:
            prediction = "fake news"
        elif ai_label == "fake news":
            prediction = "misleading"
        else:
            prediction = "real news"

        # 🔥 CONFIDENCE (IMPROVED)
        confidence = 0.5
        if rule_fake:
            confidence += 0.25
        if pattern_fake:
            confidence += 0.25
        if source_score < 0:
            confidence += 0.15
        if ai_label == "fake news":
            confidence += 0.2

        confidence = min(confidence, 1.0)

        # 🔥 REASONING (UPGRADED)
        reason = []

        if rule_fake:
            reason.append("Sensational keywords detected")

        if pattern_fake:
            reason.append("Unrealistic or exaggerated claims detected")

        if source_score < 0:
            reason.append("Untrusted or forwarded source detected")

        if ai_label == "fake news":
            reason.append("Pattern suggests misinformation")

        if not reason:
            reason.append("Looks factual and reliable")

        # 🔥 REWARD
        reward = 1.0 if action["label"] == prediction else 0.0

        return {
            "observation": {
                "prediction": prediction,
                "confidence": round(confidence, 2),
                "reason": ", ".join(reason)
            },
            "reward": reward,
            "done": True,
            "info": {"ai_prediction": ai_label}
        }