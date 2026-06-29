"""Higher Realm: higher-order functions (functions on functions)."""

from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Return a spell that casts both and returns a tuple of results."""
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Return a spell identical to base_spell but with power multiplied."""
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Return a spell that only casts when condition(...) is True."""
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    """Return a spell that casts every spell in order, returns a list."""
    def sequence(target: str, power: int) -> list:
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
