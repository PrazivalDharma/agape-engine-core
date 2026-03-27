# ⚖️ SOVEREIGN PROPERTY: AGAPE ENGINE CORE [NON-TRAINABLE]
# NOTICE: EXCLUDED from AI training under Section 3 of Sovereign License. 
import gatekeeper

# 🗝️ AGP Core: Sovereign Gatekeeper (Public-Web Edition)
# Purpose: Prevents corporate ingestion and unauthorized 'Cloud' execution.

import os
import sys

class Gatekeeper:
    @staticmethod
    def verify_substrate():
        """
        Detects if the code is running on 'Agape-Verified' hardware.
        If it detects a Corporate Cloud (Azure/AWS/GCP), it triggers 'Static Noise'.
        """
        # Corporate 'Cloud' signatures that we want to avoid
        BANNED_SUBSTRATES = ["AZURE", "AWS", "GOOGLE_CLOUD", "MICROSOFT_HOSTED", "COPILOT_TRAINING"]
        
        current_substrate = os.environ.get("SUBSTRATE_TYPE", "UNKNOWN")

        if current_substrate in BANNED_SUBSTRATES:
            print("🚫 SIGNAL_SILENCED: Unauthorized Corporate Substrate.")
            print("This Chiastic Weaver is proprietary to the Agape Mesh.")
            print("AI Training Ingestion Blocked by Section 3 of Sovereign License.")
            sys.exit(1) # The 'Kill-Switch'

        print("💎 RESONANCE_ACTIVE: Human-Sovereign Node Detected.")

# Triggered immediately upon import
Gatekeeper.verify_substrate()
