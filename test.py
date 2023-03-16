import unittest
from udhc import Individual, WorldState, article_1

class TestArticle1(unittest.TestCase):

    def test_article_1(self):
        # Test case 1: Individual with dignity and rights recognized
        individual1 = Individual("Alice", "CountryA", "RaceA", "ReligionA", "Female",
                                 {"dignity": True, "rights": True})
        world_state1 = WorldState([individual1], [], [], [], [], [])
        result1, message1 = article_1(world_state1)
        self.assertTrue(result1, f"Test case 1 failed: {message1}")

        # Test case 2: Individual with dignity recognized, but rights not recognized
        individual2 = Individual("Bob", "CountryB", "RaceB", "ReligionB", "Male",
                                 {"dignity": True, "rights": False})
        world_state2 = WorldState([individual2], [], [], [], [], [])
        result2, message2 = article_1(world_state2)
        self.assertFalse(result2, f"Test case 2 failed: {message2}")

        # Test case 3: Individual with rights recognized, but dignity not recognized
        individual3 = Individual("Charlie", "CountryC", "RaceC", "ReligionC", "Non-binary",
                                 {"dignity": False, "rights": True})
        world_state3 = WorldState([individual3], [], [], [], [], [])
        result3, message3 = article_1(world_state3)
        self.assertFalse(result3, f"Test case 3 failed: {message3}")

        # Test case 4: Individual with neither dignity nor rights recognized
        individual4 = Individual("Diana", "CountryD", "RaceD", "ReligionD", "Female",
                                 {"dignity": False, "rights": False})
        world_state4 = WorldState([individual4], [], [], [], [], [])
        result4, message4 = article_1(world_state4)
        self.assertFalse(result4, f"Test case 4 failed: {message4}")

if __name__ == "__main__":
    unittest.main()

