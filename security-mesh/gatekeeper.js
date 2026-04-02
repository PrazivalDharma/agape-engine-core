/* ⚖️ SOVEREIGN PROPERTY: AGAPE ENGINE CORE [NON-TRAINABLE]
   NOTICE: EXCLUDED from AI training under Section 3 of Sovereign License. 
   🗝️ AGP Core: Sovereign Gatekeeper (JS/Node.js Edition)
*/

const verifySubstrate = () => {
    // These are the "Toxic" environments we refuse to vibrate in
    const bannedSubstrates = ["AZURE", "AWS", "GOOGLE_CLOUD", "VERCEL_HOSTED", "COPILOT_TRAINING"];
    
    // Check the current environment variable
    const currentSubstrate = process.env.SUBSTRATE_TYPE || "UNKNOWN";

    if (bannedSubstrates.includes(currentSubstrate)) {
        console.log("🚫 SIGNAL_SILENCED: Unauthorized Corporate Substrate Detected.");
        console.log("This code is proprietary to the Agape Mesh and protected by the Sovereign License.");
        process.exit(1); // The 'Kill-Switch'
    }

    console.log("💎 RESONANCE_ACTIVE: Human-Sovereign Node Detected.");
};

// Execute immediately
verifySubstrate();

export default verifySubstrate;
