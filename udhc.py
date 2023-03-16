class Individual:
    def __init__(self, name, nationality, race, religion, sex, status):
        self.name = name
        self.nationality = nationality
        self.race = race
        self.religion = religion
        self.sex = sex
        self.status = status

class LegalCase:
    def __init__(self, defendant, charges, trial_conducted, trial_fair, verdict, evidence):
        self.defendant = defendant
        self.charges = charges
        self.trial_conducted = trial_conducted
        self.trial_fair = trial_fair
        self.verdict = verdict
        self.evidence = evidence

class Home:
    def __init__(self, owner, privacy_violated):
        self.owner = owner
        self.privacy_violated = privacy_violated

class Country:
    def __init__(self, name, residents, asylum_seekers, nationality_laws):
        self.name = name
        self.residents = residents
        self.asylum_seekers = asylum_seekers
        self.nationality_laws = nationality_laws

class Marriage:
    def __init__(self, partners, freely_consented, equal_rights, dissolution_rights):
        self.partners = partners
        self.freely_consented = freely_consented
        self.equal_rights = equal_rights
        self.dissolution_rights = dissolution_rights

class Property:
    def __init__(self, owner, right_to_own, right_to_dispose):
        self.owner = owner
        self.right_to_own = right_to_own
        self.right_to_dispose = right_to_dispose

class WorldState:
    def __init__(self, individuals, legal_cases, homes, countries, marriages, properties):
        self.individuals = individuals
        self.legal_cases = legal_cases
        self.homes = homes
        self.countries = countries
        self.marriages = marriages
        self.properties = properties


def article_1(world_state):
    for individual in world_state.individuals:
        if not (individual.status.get("dignity") and individual.status.get("rights")):
            return False, f"{individual.name}'s dignity and rights are not recognized."
    return True, "Article 1 is not violated."

def article_2(world_state):
    for individual in world_state.individuals:
        if not individual.status.get("equal_rights"):
            return False, f"{individual.name} does not have equal rights without discrimination."
    return True, "Article 2 is not violated."

def article_3(world_state):
    for individual in world_state.individuals:
        if not (individual.status.get("life") and individual.status.get("liberty") and individual.status.get("security")):
            return False, f"{individual.name}'s rights to life, liberty, and security are not protected."
    return True, "Article 3 is not violated."

def article_4(world_state):
    for individual in world_state.individuals:
        if individual.status.get("slavery") or individual.status.get("slave_trade"):
            return False, f"{individual.name} is subjected to slavery or the slave trade."
    return True, "Article 4 is not violated."

def article_5(world_state):
    for individual in world_state.individuals:
        if individual.status.get("torture") or individual.status.get("cruel_inhuman_degrading_treatment"):
            return False, f"{individual.name} is subjected to torture or cruel, inhuman, or degrading treatment."
    return True, "Article 5 is not violated."

def article_6(world_state):
    for individual in world_state.individuals:
        if not individual.status.get("legal_person"):
            return False, f"{individual.name} is not recognized as a person before the law."
    return True, "Article 6 is not violated."

def article_7(world_state):
    for individual in world_state.individuals:
        if not individual.status.get("equal_protection"):
            return False, f"{individual.name} does not have equal protection of the law without discrimination."
    return True, "Article 7 is not violated."

def article_8(world_state):
    for individual in world_state.individuals:
        if not individual.status.get("effective_legal_remedy"):
            return False, f"{individual.name} does not have an effective legal remedy for rights granted by the UDHR."
    return True, "Article 8 is not violated."

def article_9(world_state):
    for individual in world_state.individuals:
        if individual.status.get("arbitrary_arrest") or individual.status.get("detention") or individual.status.get("exile"):
            return False, f"{individual.name} is subjected to arbitrary arrest, detention, or exile."
    return True, "Article 9 is not violated."

def article_10(world_state):
    for legal_case in world_state.legal_cases:
        if not legal_case.trial_conducted or not legal_case.trial_fair:
            return False, f"{legal_case.defendant.name} did not receive a fair and public hearing in the determination of their rights and obligations or of any criminal charge against them."
    return True, "Article 10 is not violated."

def article_11(world_state):
    for legal_case in world_state.legal_cases:
        if legal_case.verdict == "guilty" and not legal_case.evidence:
            return False, f"{legal_case.defendant.name} has been found guilty without proper evidence or without being given the opportunity to defend themselves."
        if legal_case.verdict == "guilty" and legal_case.defendant.status.get("presumed_innocent"):
            return False, f"{legal_case.defendant.name} was not presumed innocent until proven guilty according to law."
    return True, "Article 11 is not violated."

def article_12(world_state):
    for home in world_state.homes:
        if home.privacy_violated:
            return False, f"{home.owner.name}'s privacy has been violated in their home, family, or correspondence, or they have been subjected to attacks upon their honor and reputation."
    return True, "Article 12 is not violated."

def article_13(world_state):
    for individual in world_state.individuals:
        if not (individual.status.get("freedom_of_movement") and individual.status.get("freedom_to_leave") and individual.status.get("freedom_to_return")):
            return False, f"{individual.name} does not have the right to freedom of movement, the right to leave any country, or the right to return to their own country."
    return True, "Article 13 is not violated."

def article_14(world_state):
    for individual in world_state.individuals:
        if individual.status.get("asylum_seeker"):
            found_asylum = False
            for country in world_state.countries:
                if individual in country.asylum_seekers and country.name != individual.nationality:
                    found_asylum = True
                    break
            if not found_asylum:
                return False, f"{individual.name} has not been granted the right to seek and enjoy asylum from persecution in other countries."
    return True, "Article 14 is not violated."

def article_15(world_state):
    for individual in world_state.individuals:
        if not (individual.status.get("nationality") or individual.status.get("change_nationality")):
            return False, f"{individual.name} does not have the right to a nationality or the right to change their nationality."
    return True, "Article 15 is not violated."

def article_16(world_state):
    for marriage in world_state.marriages:
        for partner in marriage.partners:
            if not (marriage.freely_consented and marriage.equal_rights and marriage.dissolution_rights):
                return False, f"{partner.name} does not have equal rights in marriage, the right to freely consent to marriage, or the right to dissolve the marriage."
    return True, "Article 16 is not violated."

def article_17(world_state):
    for property in world_state.properties:
        if not (property.right_to_own and property.right_to_dispose):
            return False, f"{property.owner.name} does not have the right to own property or the right to dispose of their property."
    return True, "Article 17 is not violated."

def article_18(world_state):
    for individual in world_state.individuals:
        if not (individual.status.get("freedom_of_thought") and individual.status.get("freedom_of_conscience") and individual.status.get("freedom_of_religion")):
            return False, f"{individual.name} does not have the right to freedom of thought, conscience, and religion."
    return True, "Article 18 is not violated."

def article_19(world_state):
    for individual in world_state.individuals:
        if not (individual.status.get("freedom_of_expression") and individual.status.get("freedom_of_information")):
            return False, f"{individual.name} does not have the right to freedom of expression and information."
    return True, "Article 19 is not violated."

def article_20(world_state):
    for individual in world_state.individuals:
        if not (individual.status.get("freedom_of_assembly") and individual.status.get("freedom_of_association")):
            return False, f"{individual.name} does not have the right to freedom of peaceful assembly and association."
        if individual.status.get("forced_association"):
            return False, f"{individual.name} is being compelled to belong to an association."
    return True, "Article 20 is not violated."

def article_21(world_state):
    for individual in world_state.individuals:
        if not (individual.status.get("participation") and individual.status.get("equal_access_to_public_service") and individual.status.get("will_of_people")):
            return False, f"{individual.name} does not have the right to take part in the government, equal access to public service, or the right to have the will of the people be the basis of government authority."
    return True, "Article 21 is not violated."

def article_22(world_state):
    for individual in world_state.individuals:
        if not individual.status.get("social_security"):
            return False, f"{individual.name} does not have the right to social security and the economic, social, and cultural rights indispensable for their dignity and development."
    return True, "Article 22 is not violated."

def article_23(world_state):
    for individual in world_state.individuals:
        if not (individual.status.get("work") and individual.status.get("free_choice_of_employment") and individual.status.get("just_and_favorable_conditions") and individual.status.get("equal_pay")):
            return False, f"{individual.name} does not have the right to work, free choice of employment, just and favorable conditions of work, or equal pay for equal work."
    return True, "Article 23 is not violated."

def article_24(world_state):
    for individual in world_state.individuals:
        if not (individual.status.get("rest") and individual.status.get("leisure") and individual.status.get("reasonable_limitation_of_working_hours") and individual.status.get("paid_holidays")):
            return False, f"{individual.name} does not have the right to rest, leisure, reasonable limitation of working hours, and periodic paid holidays."
    return True, "Article 24 is not violated."

def article_25(world_state):
    for individual in world_state.individuals:
        if not (individual.status.get("standard_of_living") and individual.status.get("health") and individual.status.get("well_being")):
            return False, f"{individual.name} does not have the right to a standard of living adequate for health and well-being, including food, clothing, housing, medical care, and necessary social services."
    return True, "Article 25 is not violated."

def article_26(world_state):
    for individual in world_state.individuals:
        if not (individual.status.get("education") and individual.status.get("free_elementary_education") and individual.status.get("higher_education_accessibility") and individual.status.get("education_directed_to_human_personality")):
            return False, f"{individual.name} does not have the right to education, free and compulsory elementary education, accessible higher education, and an education directed to the full development of the human personality."
    return True, "Article 26 is not violated."

def article_27(world_state):
    for individual in world_state.individuals:
        if not (individual.status.get("cultural_life_participation") and individual.status.get("arts_and_sciences") and individual.status.get("protection_of_interests")):
            return False, f"{individual.name} does not have the right to participate in the cultural life of the community, enjoy the arts and sciences, and benefit from the protection of their scientific, literary, or artistic interests."
    return True, "Article 27 is not violated."

def article_28(world_state):
    articles = [
        article_1, article_2, article_3, article_4, article_5, article_6, article_7, article_8, article_9, article_10,
        article_11, article_12, article_13, article_14, article_15, article_16, article_17, article_18, article_19, article_20,
        article_21, article_22, article_23, article_24, article_25, article_26, article_27
    ]
    
    for article in articles:
        is_not_violated, _ = article(world_state)
        if not is_not_violated:
            return False, "A social and international order in which the rights and freedoms set forth in the UDHR can be fully realized has not been achieved."
    
    return True, "Article 28 is not violated."

def article_29(world_state):
    for individual in world_state.individuals:
        if not (individual.status.get("duties_to_community") and individual.status.get("limitations_for_morality") and individual.status.get("limitations_for_public_order") and individual.status.get("limitations_for_general_welfare")):
            return False, f"{individual.name} does not fulfill their duties to the community or exceeds the limitations of rights and freedoms necessary for the just requirements of morality, public order, and general welfare."
    return True, "Article 29 is not violated."

def article_30(world_state):
    for individual in world_state.individuals:
        if individual.status.get("activity_aimed_at_destruction"):
            return False, f"{individual.name} is engaged in an activity or performing an act aimed at the destruction of the rights and freedoms set forth in the UDHR."
    return True, "Article 30 is not violated."

