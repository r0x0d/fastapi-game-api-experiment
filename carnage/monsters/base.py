from functools import cached_property

from carnage.database.models.monster import MonsterModel


class BaseMonster:
    def __init__(self, monster: MonsterModel) -> None:
        self.monster = monster
        self.current_hitpoints = monster.hitpoints
        self.normal_attack = 1
        self.critical_attack = 2
        self.attack_threshold = 40
        self.critical_attack_threshold = 95

    def take_damage(self, damage: int) -> None:
        self.current_hitpoints -= damage

    def attack(self, player_defense: int) -> int:
        # Apply the hit chance here
        damage = (
            self.damage_type
            * self.monster.base_damage
            / ((100 + player_defense) / 100)
        )

        return damage

    def magical_attack(self, player_magical_defense: int) -> int:
        # Apply the hit chance here
        damage = (
            self.damage_type
            * 2
            * self.monster.base_magical_damage
            * self.monster.base_magical_damage
            / (self.monster.base_magical_damage + player_magical_defense)
        )

        return damage

    def can_perform_attack(self, player_dexterity: int) -> bool:
        attack_percentage = (player_dexterity / self.monster.dexterity) * 100
        return attack_percentage >= self.attack_threshold

    def can_perform_critical_attack(self, player_dexterity: int) -> bool:
        critical_attack_percentage = (
            player_dexterity + (player_dexterity / 4)
        ) - (self.monster.dexterity + (self.monster.dexterity / 4))

        return critical_attack_percentage >= self.critical_attack_threshold

    @property
    def damage_type(self) -> int:
        # Apply the critical chance here
        return self.normal_attack or self.critical_attack

    @cached_property
    def is_alive(self) -> bool:
        return self.current_hitpoints <= 0
