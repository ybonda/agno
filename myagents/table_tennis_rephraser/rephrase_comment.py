"""
Table Tennis Equipment Comment Rephraser Agent

This agent uses OpenRouter to rephrase customer comments about table tennis equipment
in a more human-like manner while preserving the main logic and sentiment.
"""

from pathlib import Path
from typing import List

from agno.agent import Agent, RunOutput
from agno.models.openrouter import OpenRouter
from dotenv import load_dotenv
from pydantic import BaseModel, Field

# Load environment variables from .env file at project root
project_root = Path(__file__).parent.parent.parent
env_path = project_root / ".env"
load_dotenv(env_path)


class RephraseResult(BaseModel):
    """Structured output for rephrased comments."""

    original_comment: str = Field(..., description="The original customer comment")
    rephrased_comment: str = Field(
        ...,
        description="The rephrased comment in a natural, human-like manner",
    )
    key_points: List[str] = Field(
        ...,
        description="Main points and logic preserved from the original comment",
    )


# Create the rephraser agent with structured output
rephraser_agent = Agent(
    name="Table Tennis Comment Rephraser",
    model=OpenRouter(
        # id="anthropic/claude-3-haiku", #
        id="deepseek/deepseek-chat-v3-0324", # very good, price: 0.000663
        # id="z-ai/glm-4.6", # slow, price: 0.00107
        # id="mistralai/mixtral-8x7b-instruct", # failed 3 times, price: 0.000499
    ),
    description="Expert at rephrasing table tennis equipment customer comments in a natural, human-like manner.",
    instructions=[
        "You are a professional copywriter specializing in table tennis equipment reviews.",
        "Your task is to rephrase customer comments to sound more natural and human-like.",
        "Always preserve the core message, sentiment (positive/negative), and technical details.",
        "Maintain authenticity - the rephrased comment should sound like a real person wrote it.",
        "Keep the same level of enthusiasm or criticism as the original.",
        "Preserve specific product names, brands, and technical specifications mentioned.",
        "Make the comment more readable and engaging while staying true to the original intent.",
        "Use natural language patterns and varied sentence structures.",
        "If the comment is not in English, translate it to English first.",
    ],
    # output_schema=RephraseResult,
    markdown=True,
    debug_mode=True,
)


def rephrase_comment(comment: str) -> RephraseResult:
    """
    Rephrase a single customer comment.

    Args:
        comment: The original customer comment to rephrase

    Returns:
        RephraseResult: Structured result with original, rephrased comment, and key points
    """
    response: RunOutput = rephraser_agent.run(
        f"Rephrase this table tennis equipment customer comment:\n\n{comment}"
    )
    return response.content


def rephrase_comments_batch(comments: List[str]) -> List[RephraseResult]:
    """
    Rephrase multiple customer comments efficiently.

    Note: This reuses the same agent instance for better performance (529× faster than recreating).

    Args:
        comments: List of customer comments to rephrase

    Returns:
        List[RephraseResult]: List of rephrased results
    """
    results = []
    for comment in comments:
        response: RunOutput = rephraser_agent.run(
            f"Rephrase this table tennis equipment customer comment:\n\n{comment}"
        )
        results.append(response.content)
    return results


if __name__ == "__main__":
    # Example usage
    # sample_comments = [
    #     "I highly recommend this blade because I'm a true geek who loves trying different blades. To be honest, I'm not a professional player — just a hobbyist — but I'm pretty good and know all the fundamentals.\n\nIf you're someone shifting from an all-wood blade and looking for more control, this blade is a great option. Despite being a controlled blade, it still feels fast — I've played with Dignics 05 and MX-P on it, and the control is still very much there.\n\nIn conclusion, this blade is well-suited for players who enjoy blocking, counter-attacking, and want a balanced setup. Amateur players who feel that outer-force blades are too fast will really appreciate the comfort and control this blade offers.",
    # ]
    # sample_comments = [
    #     "Comparing to Viscaria-type:\n\nFeeling more on the soft side, but crunchy when hit hard. A bit top-heavy, a bit stiff & thick. Short game easy to control and spin as blade isn't fast there, but harder to control spin-ups and loops as it is a bit stiff. High potential for top-end power.\n\nFor hard hitters who want top-end power with a softer feel for spin/touch shots. Suits Anders Lind's style - makes sense!\n\nI however prefer a thinner/flexier blade for consistency in spin-ups and close to table topspin as that is my game.",
    # ]
    # sample_comments = [
    #     "Cambie de una madera Butterfly Gergely Alpha a esta de Anders Lind, en general te da mayor confianza en cada golpe, casi todo entra en la mesa, es excelente para tospin, smash, juego corto, quizás los bloqueos pasivos no sean tan bueno como la Gergely pero con un pequeño ajuste es fácil acostumbrase, tiene buen control que permite hacer incluso buenos chops, le arme con victas v>22 double extra 2.0 en forehand y omega v tour 2.1 en revés, quedo perfecto, también le iría bien la banco power ultimate 50 o incluso la misma omega v tour antes mencionada en forehand. Lo único negativo pero es más algo personal es el peso de la madera 89.5g, me hubiera gustado conseguir una versión algo más ligera. En conclusión se la recomiendo desde principiantes hasta avanzados",
    # ]
    # sample_comments = [
    #     "Paired it with hybrid and tensor rubbers. The racket itself is surprisingly bouncy and light - mine was ~85g - so drives and loops were fast enough. Performance was better with a more direct contact for loops than brushing. That being said, don't expect outer carbon levels of speed. The upper limit is not as high. It does best with moderate level effort strokes (60-80% effort).\n\nShort game is very good and retains the wood feeling. Close to the table play is also very controllable. Bh flicks are not super fast, but can reliably get you into the rally.\n\nOverall doesn't have insane killing power, is dangerous close to the table and fairly safe/consistent when away from the table.",
    # ]
    # sample_comments = [
    #     "De las mejores paletas que he usado, una maravilla todoterreno. Sirve para el juego corto, buen bloqueo y buena velocidad cuando se la acelera junto con un control que no se puede creer. Hasta el momento es la mejor paleta que he usado.",
    # ]
    sample_comments = [
        "I think this is a very accurate description of the blade!\n\nI've been playing with it for a few weeks and I really like it; it can be quite fast, but I always feel it provides a lot of control. Perhaps it's due to the choice of wood (outer koto and limba underneath), or maybe it's the mysterious hexa carbon next to the kiri core.\n\nDoes anyone happen to have information about what this 'hexa carbon' actually is? It sounds quite enigmatic; Donic doesn't describe this technology, and it seems they used it for the first time in the blade. Is it pure carbon, or perhaps a mix of carbon and something else? I get the impression that it's quite soft, there's no feeling of metallicness or stiffness.",
    ]
    print("=" * 80)
    print("Table Tennis Equipment Comment Rephraser")
    print("=" * 80)
    print()

    # Single comment example
    print("Single Comment Example:")
    print("-" * 80)
    result = rephrase_comment(sample_comments[0])
    # print(f"Original: {result.original_comment}")
    # print(f"\nRephrased: {result.rephrased_comment}")
    # print(f"\nKey Points: {', '.join(result.key_points)}")
    print(f"\nRephrased: {result}")
    print()

    # Batch processing example
    # print("\n" + "=" * 80)
    # print("Batch Processing Example (All Comments):")
    # print("=" * 80)
    # results = rephrase_comments_batch(sample_comments)

    # for i, result in enumerate(results, 1):
    #     print(f"\n--- Comment {i} ---")
    #     print(f"Original: {result.original_comment}")
    #     print(f"Rephrased: {result.rephrased_comment}")
    #     print()
