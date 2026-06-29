"""Higher Realm: higher-order functions (functions on functions)."""

from collections.abc import Callable

# The spell contract: every spell takes (target, power) and returns a string.
Spell = Callable[[str, int], str]


def spell_combiner(
    spell1: Spell, spell2: Spell
) -> Callable[[str, int], tuple[str, str]]:
    """Return a spell that casts both and returns a tuple of results."""
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    """Return a spell identical to base_spell but with power multiplied."""
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(
    condition: Callable[[str, int], bool], spell: Spell
) -> Spell:
    """Return a spell that only casts when condition(...) is True."""
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Spell]) -> Callable[[str, int], list[str]]:
    """Return a spell that casts every spell in order, returns a list."""
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def main() -> None:
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power}"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power}"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined('Dragon', 10)}")

    print("Testing power amplifier...")
    mega = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon', 10)}")
    print(f"Amplified: {mega('Dragon', 10)}")

    print("Testing conditional caster...")
    strong = conditional_caster(lambda t, p: p >= 50, fireball)
    print(strong('Goblin', 10))
    print(strong('Goblin', 80))

    print("Testing spell sequence...")
    seq = spell_sequence([fireball, heal])
    print(seq('Knight', 25))


if __name__ == "__main__":
    main()
