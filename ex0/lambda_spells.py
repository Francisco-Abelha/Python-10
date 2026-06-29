"""Lambda Sanctum: mastering anonymous functions."""


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort artifacts by 'power' (descending) using a lambda key."""
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Keep only mages whose 'power' is >= min_power."""
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Wrap each spell name as '* name *'."""
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Return {'max_power', 'min_power', 'avg_power'} for the mages."""
    powers = list(map(lambda m: m['power'], mages))
    return {
        'max_power': max(mages, key=lambda m: m['power'])['power'],
        'min_power': min(mages, key=lambda m: m['power'])['power'],
        'avg_power': round(sum(powers) / len(mages), 2),
    }


def main() -> None:
    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
    ]
    mages = [
        {'name': 'Alex', 'power': 70, 'element': 'fire'},
        {'name': 'Riley', 'power': 95, 'element': 'ice'},
    ]

    print("Testing artifact sorter...")
    ordered = artifact_sorter(artifacts)
    print(f"{ordered[0]['name']} ({ordered[0]['power']} power) comes before "
          f"{ordered[1]['name']} ({ordered[1]['power']} power)")

    print("Testing spell transformer...")
    print(' '.join(spell_transformer(['fireball', 'heal', 'shield'])))

    print("Testing power filter...")
    print(power_filter(mages, 80))

    print("Testing mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
