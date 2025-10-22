from doctest import debug
import json
import logging
from pathlib import Path
from typing import Any, Dict, List

from dotenv import load_dotenv

from agno.agent import Agent
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.models.perplexity import Perplexity

from agno.models.openrouter import OpenRouter

# from agno.vectordb.qdrant import Qdrant

# Load environment variables from .env file at project root
project_root = Path(__file__).parent.parent.parent
env_path = project_root / ".env"
load_dotenv(env_path)


if __name__ == "__main__":

    agent = Agent(
        # model=Perplexity(id="sonar-pro"),
        model=OpenRouter(
            # id="perplexity/sonar-pro",
            id="perplexity/sonar",
            # id="anthropic/claude-haiku-4.5", # 0.00195
        ),
        markdown=True,
        debug_mode=True,
    )

    # Test with the original query
    agent.print_response("Get technical specifications and features of DONIC Anders Lind Hexa Carbon blade.")
    # agent.print_response("Compare DONIC Anders Lind Hexa Carbon blade with Butterfly Primorac Carbon")
    # agent.print_response("Get technical specifications and features of Butterfly Zyre03 rubber.")
    # agent.print_response("Give me a summary YANG WANG (SVK), his playing style and his equipment, his highest rank in the world.")
    # agent.print_response("What are prices for DONIC Anders Lind Hexa Carbon blade.")
    # agent.print_response("What are pricing plans of https://humanizerai.com/ and what are the features of each plan.")
    # agent.print_response("What is hardness of Donic BlueFire C2 rubber? In Japanese scale and ESN scale.")

# -----------sonar ------------------
# ┃                                                                                                 Technical Specifications and Features of DONIC Anders Lind Hexa Carbon Blade                                                                                                 ┃
# ┃                                                                                                                                                                                                                                                                              ┃
# ┃                                                                                                                                   Overview                                                                                                                                   ┃
# ┃                                                                                                                                                                                                                                                                              ┃
# ┃ The DONIC Anders Lind Hexa Carbon is a high-end, 7-layer OFF (offensive) table tennis blade designed in collaboration with Danish player Anders Lind. It offers a combination of speed, control, and dynamic playability.                                                    ┃
# ┃                                                                                                                                                                                                                                                                              ┃
# ┃                                                                                                                              Key Specifications                                                                                                                              ┃
# ┃                                                                                                                                                                                                                                                                              ┃
# ┃  • Layers: 7 layers with a Kiri core, surrounded by Hexamid Carbon on the inside, and Limba and Koto wood on the outside.                                                                                                                                                    ┃
# ┃  • Speed: 93                                                                                                                                                                                                                                                                 ┃
# ┃  • Control: 71                                                                                                                                                                                                                                                               ┃
# ┃  • Thickness: Approximately 5.6 mm                                                                                                                                                                                                                                           ┃
# ┃  • Weight: Generally 80-90 grams, with a listed weight of 87 grams                                                                                                                                                                                                           ┃
# ┃  • Handles: Available in FL (Flared) and ST (Straight) styles                                                                                                                                                                                                                ┃
# ┃  • Material: Wood + Composite (Hexamid Carbon)                                                                                                                                                                                                                               ┃
# ┃                                                                                                                                                                                                                                                                              ┃
# ┃                                                                                                                                   Features                                                                                                                                   ┃
# ┃                                                                                                                                                                                                                                                                              ┃
# ┃  • Inner Composite Design: The blade features an inner composite structure with Hexamid Carbon layers, providing stability and control.                                                                                                                                      ┃
# ┃  • Outer Wood Layers: Limba and Koto wood plies enhance the blade's power and sensitivity.                                                                                                                                                                                   ┃
# ┃  • Visual Design: The handle is designed in the Danish national colors, adding a unique aesthetic appeal.                                                                                                                                                                    ┃
# ┃  • Performance: Suitable for offensive players, offering a balance of speed and control, making it ideal for players seeking dynamic play with manageable power.                                                                                                             ┃
# ┃                                                                                                                                                                                                                                                                              ┃
# ┃                                                                                                                              Player Suitability                                                                                                                              ┃
# ┃                                                                                                                                                                                                                                                                              ┃
# ┃  • Recommended for: Intermediate to advanced players who prefer a fast yet controllable setup, particularly those focusing on loop play and counter-attacks.


#  sonar-pro
#
#  price: 0.0167

# ┃ Butterfly Zyre03 is a high-performance offensive table tennis rubber designed for maximal spin, power, and durability, featuring a unique top sheet and thickened sponge technology optimized for aggressive rally play[1][2][3][5][7][9].               ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃ Technical Specifications                                                                                                                                                                                                                                 ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃   Specification       Value                                                                                                                                                                                                                              ┃
# ┃  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                                                                                                                                          ┃
# ┃   Type                High Tension pimples-in                                                                                                                                                                                                            ┃
# ┃   Technology          High Tension, Spring Sponge X, Ricosheet                                                                                                                                                                                           ┃
# ┃   Top Sheet           Ricosheet (dense, low pimples, No. 303)                                                                                                                                                                                            ┃
# ┃   Sponge Hardness     44 (harder, for extra kick/solid feel)                                                                                                                                                                                             ┃
# ┃   Speed               88                                                                                                                                                                                                                                 ┃
# ┃   Spin                100 (maximum in Butterfly lineup)                                                                                                                                                                                                  ┃
# ┃   Arc                 96                                                                                                                                                                                                                                 ┃
# ┃   Thickness           2.7 mm / 2.5 mm                                                                                                                                                                                                                    ┃
# ┃   Colors              Red, Black                                                                                                                                                                                                                         ┃
# ┃   Country of Origin   Japan                                                                                                                                                                                                                              ┃
# ┃   Code                06140                                                                                                                                                                                                                              ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃ Key Features                                                                                                                                                                                                                                             ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃  • Dense, low-profile pimples in the Ricosheet top sheet provide explosive spin and high power output[2][5][7].                                                                                                                                          ┃
# ┃  • Harder, extra-thick Spring Sponge X maximizes rebound, shot depth, and arc. Thicker sponge optimizes energy transfer while keeping overall weight manageable, due to aerated rubber material[3][9].                                                   ┃
# ┃  • Durability: The short-profile, high-density pimples yield about 40% higher surface strength versus Butterfly Dignics 05, protecting against tearing and abrasion—even under heavy impact[3].                                                          ┃
# ┃  • Ball grip & feel: Enhanced compound holds the ball longer, improving control and flexibility. The thicker sponge, thin top sheet combo delivers a surprisingly softer feel and quieter sound, atypical for such hard rubbers[3].                      ┃
# ┃  • Playing style: Targeted for aggressive loopers and players who dominate rallies with high power and heavy spin[1][2][7].                                                                                                                              ┃
# ┃  • Weight: Maintains lightness despite a thicker sponge, supporting fast swing speeds and easier blade-rubber combinations[3].                                                                                                                           ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃ Comparison with Other Butterfly Rubbers                                                                                                                                                                                                                  ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃   Rubber       Speed   Spin   Sponge Hardness   Sponge Thickness (max)                                                                                                                                                                                   ┃
# ┃  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                                                                                                                                  ┃
# ┃   Zyre 03      88      100    44                2.7 mm                                                                                                                                                                                                   ┃
# ┃   Dignics 05   84      97     40                2.1 mm                                                                                                                                                                                                   ┃
# ┃   Tenergy 05   90      90     36                2.1 mm                                                                                                                                                                                                   ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃ Summary of Innovations                                                                                                                                                                                                                                   ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃  • Ricosheet top sheet with pimple code No. 303 for optimal power-spin balance[1][2].                                                                                                                                                                    ┃
# ┃  • Spring Sponge X delivers extra firmness and enhanced rebound[1][5][7].                                                                                                                                                                                ┃
# ┃  • Maintains control and durability for high-impact professional play[3][5].                                                                                                                                                                             ┃
# ┃  • Butterfly's most spin-capable rubber, ideal for advanced offensive strategies[1][6].                                                                                                                                                                  ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃ Zyre03 is recommended for top-level players seeking maximum spin, offensive rebound, and resilience in their equipment.     


# -----------------------------

# sonar
#
# price: 0.00577

# ┃ The Butterfly Zyre 03 rubber is a high-performance table tennis rubber featuring a unique combination of technologies for enhanced power, spin, durability, and control. Its key technical specifications and features are:                              ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃  • Type: High Tension pimples-in rubber                                                                                                                                                                                                                  ┃
# ┃  • Technologies: High Tension, Spring Sponge X, Ricosheet                                                                                                                                                                                                ┃
# ┃  • Speed rating: 88                                                                                                                                                                                                                                      ┃
# ┃  • Spin rating: 100                                                                                                                                                                                                                                      ┃
# ┃  • Arc: 96 (trajectory of the ball when hit)                                                                                                                                                                                                             ┃
# ┃  • Sponge hardness: 44 (medium-hard sponge)                                                                                                                                                                                                              ┃
# ┃  • Sponge thickness options: 2.5 mm or 2.7 mm                                                                                                                                                                                                            ┃
# ┃  • Sheet color: Available in red and black                                                                                                                                                                                                               ┃
# ┃  • Country of origin: Japan[1][2][3][5][9]                                                                                                                                                                                                               ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃                                                                                                                    Detailed Features:                                                                                                                    ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃  • Ricosheet Top Sheet: Made of dense, low pimples (short-profile pimples) that increase durability and reduce damage risk from strong impacts and table hits. This design also enhances the "grip" on the ball to produce powerful spin and controlled  ┃
# ┃    shots[1][2][3].                                                                                                                                                                                                                                       ┃
# ┃  • Extra-Thick Sponge (Spring Sponge X): Zyre 03 has a thicker sponge (2.5 or 2.7 mm) compared to many rubbers. The sponge is made from an aerated rubber material that balances high deformation and high rebound. This means it grips the ball firmly  ┃
# ┃    and releases it explosively for strong spin and speed[1][2][4].                                                                                                                                                                                       ┃
# ┃  • Improved Durability and Abrasion Resistance: The top sheet compound is enhanced for resistance to abrasion and maintains durability even under repetitive heavy impact, about 40% stronger in surface strength than Butterfly Dignics 05 in internal  ┃
# ┃    testing[1][3].                                                                                                                                                                                                                                        ┃
# ┃  • Optimized Rebound and Shot Trajectory: The combination of a thin but dense top sheet with a thick sponge optimizes energy transfer, reducing ball deformation and leading to more solid, powerful strikes with a dramatic, high arc                   ┃
# ┃    trajectory[1][2][3].                                                                                                                                                                                                                                  ┃
# ┃  • Playing Style Suitability: Recommended for players seeking to dominate rallies with powerful spin-heavy shots. The rubber heightens spin potential and control, suitable for forehand and powerful backhand strokes with sufficient                   ┃
# ┃    technique[2][4][8].                                                                                                                                                                                                                                   ┃
# ┃  • Weight: Despite the thick sponge, the 2.7 mm version is only about 1 gram heavier than the thinner Dignics 05, helping maintain swing speed and flexibility in blade combinations[4].                                                                 ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃                                                                                                                      Summary Table                                                                                                                       ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃   Feature            Specification                                                                                                                                                                                                                       ┃
# ┃  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                                                                                                                                                      ┃
# ┃   Rubber Type        High Tension pimples-in                                                                                                                                                                                                             ┃
# ┃   Technologies       High Tension, Spring Sponge X, Ricosheet                                                                                                                                                                                            ┃
# ┃   Speed              88                                                                                                                                                                                                                                  ┃
# ┃   Spin               100                                                                                                                                                                                                                                 ┃
# ┃   Arc                96                                                                                                                                                                                                                                  ┃
# ┃   Sponge Hardness    44                                                                                                                                                                                                                                  ┃
# ┃   Sponge Thickness   2.5 mm or 2.7 mm                                                                                                                                                                                                                    ┃
# ┃   Pimple Profile     Short, dense low pimples (No. 303 code)                                                                                                                                                                                             ┃
# ┃   Durability         ~40% stronger surface strength vs. Dignics 05                                                                                                                                                                                       ┃
# ┃   Recommended Use    Power and spin-focused players                                                                                                                                                                                                      ┃
# ┃   Sheet Colors       Red and black                                                                                                                                                                                                                       ┃
# ┃   Origin             Japan                                                                                                                                                                                                                               ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃                                                                                                                                                                                                                                                          ┃
# ┃ This rubber represents a revolution in rubber design for Butterfly, combining a tougher, abrasion-resistant top sheet and a thick, springy sponge to deliver both power and exceptional spin in rallies[1][2][4][5].     