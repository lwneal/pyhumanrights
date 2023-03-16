import humanrights

def create_apartheid_individuals():
    black_individual = humanrights.Individual(
        name="Black South African",
        nationality="South African",
        race="Black",
        religion=None,
        sex=None,
        status={
            "dignity": False,
            "rights": False,
            "equal_rights": False,
            "life": True,
            "liberty": False,
            "security": False,
            "torture": False,
            "cruel_inhuman_degrading_treatment": True
        }
    )

    return [black_individual]

def test_apartheid():
    # Historical context: Apartheid (1948-1994)
    # System of institutionalized racial segregation and discrimination in South Africa

    world_state = humanrights.WorldState(
        individuals=create_apartheid_individuals(),
        legal_cases=[],
        homes=[],
        countries=[],
        marriages=[],
        properties=[]
    )

    violation_article_1, message_1 = humanrights.article_1(world_state)
    assert not violation_article_1, f"Article 1 was violated: {message_1}"

    violation_article_2, message_2 = humanrights.article_2(world_state)
    assert not violation_article_2, f"Article 2 was violated: {message_2}"

    violation_article_3, message_3 = humanrights.article_3(world_state)
    assert not violation_article_3, f"Article 3 was violated: {message_3}"

    violation_article_5, message_5 = humanrights.article_5(world_state)
    assert not violation_article_5, f"Article 5 was violated: {message_5}"

