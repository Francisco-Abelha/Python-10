"""Master's Tower: decorators and staticmethods."""

import functools
import time
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator: time a spell's execution and report it."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    """Decorator factory: only run if first arg (power) >= min_power."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get("power")
            if power is None:
                power = next((a for a in args if isinstance(a, int)), 0)
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    """Decorator factory: retry a failing spell up to max_attempts times."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    """Demonstrates @staticmethod alongside an instance method."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Valid if >= 3 chars and only letters/spaces."""
        return len(name) >= 3 and all(
            c.isalpha() or c.isspace() for c in name
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell if power is sufficient (>= 10)."""
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    print("Testing spell timer...")
    print(f"Result: {fireball()}")

    print("Testing retrying spell...")
    attempts = {"n": 0}

    @retry_spell(3)
    def flaky() -> str:
        attempts["n"] += 1
        raise ValueError("boom")

    print(flaky())

    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Alex"))
    print(MageGuild.validate_mage_name("Jo"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
