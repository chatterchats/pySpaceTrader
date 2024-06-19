from enum import StrEnum, Enum


class ActivityLevel(StrEnum):
    WEAK = "WEAK"
    GROWING = "GROWING"
    STRONG = "STRONG"
    RESTRICTED = "RESTRICTED"


class ContractType(StrEnum):
    PROCUREMENT = "PROCUREMENT"
    TRANSPORT = "TRANSPORT"
    SHUTTLE = "SHUTTLE"


class DepositSymbol(StrEnum):
    QUARTZ_SAND = "QUARTZ_SAND"
    SILICON_CRYSTALS = "SILICON_CRYSTALS"
    PRECIOUS_STONES = "PRECIOUS_STONES"
    ICE_WATER = "ICE_WATER"
    AMMONIA_ICE = "AMMONIA_ICE"
    IRON_ORE = "IRON_ORE"
    COPPER_ORE = "COPPER_ORE"
    SILVER_ORE = "SILVER_ORE"
    ALUMINUM_ORE = "ALUMINUM_ORE"
    GOLD_ORE = "GOLD_ORE"
    PLATINUM_ORE = "PLATINUM_ORE"
    DIAMONDS = "DIAMONDS"
    URANITE_ORE = "URANITE_ORE"
    MERITIUM_ORE = "MERITIUM_ORE"


class FactionTraitSymbol(StrEnum):
    BUREAUCRATIC = "BUREAUCRATIC"
    SECRETIVE = "SECRETIVE"
    CAPITALISTIC = "CAPITALISTIC"
    INDUSTRIOUS = "INDUSTRIOUS"
    PEACEFUL = "PEACEFUL"
    DISTRUSTFUL = "DISTRUSTFUL"
    WELCOMING = "WELCOMING"
    SMUGGLERS = "SMUGGLERS"
    SCAVENGERS = "SCAVENGERS"
    REBELLIOUS = "REBELLIOUS"
    EXILES = "EXILES"
    PIRATES = "PIRATES"
    RAIDERS = "RAIDERS"
    CLAN = "CLAN"
    GUILD = "GUILD"
    DOMINION = "DOMINION"
    FRINGE = "FRINGE"
    FORSAKEN = "FORSAKEN"
    ISOLATED = "ISOLATED"
    LOCALIZED = "LOCALIZED"
    ESTABLISHED = "ESTABLISHED"
    NOTABLE = "NOTABLE"
    DOMINANT = "DOMINANT"
    INESCAPABLE = "INESCAPABLE"
    INNOVATIVE = "INNOVATIVE"
    BOLD = "BOLD"
    VISIONARY = "VISIONARY"
    CURIOUS = "CURIOUS"
    DARING = "DARING"
    EXPLORATORY = "EXPLORATORY"
    RESOURCEFUL = "RESOURCEFUL"
    FLEXIBLE = "FLEXIBLE"
    COOPERATIVE = "COOPERATIVE"
    UNITED = "UNITED"
    STRATEGIC = "STRATEGIC"
    INTELLIGENT = "INTELLIGENT"
    RESEARCH_FOCUSED = "RESEARCH_FOCUSED"
    COLLABORATIVE = "COLLABORATIVE"
    PROGRESSIVE = "PROGRESSIVE"
    MILITARISTIC = "MILITARISTIC"
    TECHNOLOGICALLY_ADVANCED = "TECHNOLOGICALLY_ADVANCED"
    AGGRESSIVE = "AGGRESSIVE"
    IMPERIALISTIC = "IMPERIALISTIC"
    TREASURE_HUNTERS = "TREASURE_HUNTERS"
    DEXTEROUS = "DEXTEROUS"
    UNPREDICTABLE = "UNPREDICTABLE"
    BRUTAL = "BRUTAL"
    FLEETING = "FLEETING"
    ADAPTABLE = "ADAPTABLE"
    SELF_SUFFICIENT = "SELF_SUFFICIENT"
    DEFENSIVE = "DEFENSIVE"
    PROUD = "PROUD"
    DIVERSE = "DIVERSE"
    INDEPENDENT = "INDEPENDENT"
    SELF_INTERESTED = "SELF_INTERESTED"
    FRAGMENTED = "FRAGMENTED"
    COMMERCIAL = "COMMERCIAL"
    FREE_MARKETS = "FREE_MARKETS"
    ENTREPRENEURIAL = "ENTREPRENEURIAL"


class FactionSymbol(StrEnum):
    COSMIC = "COSMIC"
    VOID = "VOID"
    GALACTIC = "GALACTIC"
    QUANTUM = "QUANTUM"
    DOMINION = "DOMINION"
    ASTRO = "ASTRO"
    CORSAIRS = "CORSAIRS"
    OBSIDIAN = "OBSIDIAN"
    AEGIS = "AEGIS"
    UNITED = "UNITED"
    SOLITARY = "SOLITARY"
    COBALT = "COBALT"
    OMEGA = "OMEGA"
    ECHO = "ECHO"
    LORDS = "LORDS"
    CULT = "CULT"
    ANCIENTS = "ANCIENTS"
    SHADOW = "SHADOW"
    ETHEREAL = "ETHEREAL"


class RefinedGoodSymbol(StrEnum):
    IRON = "IRON"
    COPPER = "COPPER"
    SILVER = "SILVER"
    GOLD = "GOLD"
    ALUMINUM = "ALUMINUM"
    PLATINUM = "PLATINUM"
    URANITE = "URANITE"
    MERITIUM = "MERITIUM"
    FUEL = "FUEL"


class ShipConditionEventSymbol(StrEnum):
    REACTOR_OVERLOAD = "REACTOR_OVERLOAD"
    ENERGY_SPIKE_FROM_MINERAL = "ENERGY_SPIKE_FROM_MINERAL"
    SOLAR_FLARE_INTERFERENCE = "SOLAR_FLARE_INTERFERENCE"
    COOLANT_LEAK = "COOLANT_LEAK"
    POWER_DISTRIBUTION_FLUCTUATION = "POWER_DISTRIBUTION_FLUCTUATION"
    MAGNETIC_FIELD_DISRUPTION = "MAGNETIC_FIELD_DISRUPTION"
    HULL_MICROMETEORITE_STRIKES = "HULL_MICROMETEORITE_STRIKES"
    STRUCTURAL_STRESS_FRACTURES = "STRUCTURAL_STRESS_FRACTURES"
    CORROSIVE_MINERAL_CONTAMINATION = "CORROSIVE_MINERAL_CONTAMINATION"
    THERMAL_EXPANSION_MISMATCH = "THERMAL_EXPANSION_MISMATCH"
    VIBRATION_DAMAGE_FROM_DRILLING = "VIBRATION_DAMAGE_FROM_DRILLING"
    ELECTROMAGNETIC_FIELD_INTERFERENCE = "ELECTROMAGNETIC_FIELD_INTERFERENCE"
    IMPACT_WITH_EXTRACTED_DEBRIS = "IMPACT_WITH_EXTRACTED_DEBRIS"
    FUEL_EFFICIENCY_DEGRADATION = "FUEL_EFFICIENCY_DEGRADATION"
    COOLANT_SYSTEM_AGEING = "COOLANT_SYSTEM_AGEING"
    DUST_MICROABRASIONS = "DUST_MICROABRASIONS"
    THRUSTER_NOZZLE_WEAR = "THRUSTER_NOZZLE_WEAR"
    EXHAUST_PORT_CLOGGING = "EXHAUST_PORT_CLOGGING"
    BEARING_LUBRICATION_FADE = "BEARING_LUBRICATION_FADE"
    SENSOR_CALIBRATION_DRIFT = "SENSOR_CALIBRATION_DRIFT"
    HULL_MICROMETEORITE_DAMAGE = "HULL_MICROMETEORITE_DAMAGE"
    SPACE_DEBRIS_COLLISION = "SPACE_DEBRIS_COLLISION"
    THERMAL_STRESS = "THERMAL_STRESS"
    VIBRATION_OVERLOAD = "VIBRATION_OVERLOAD"
    PRESSURE_DIFFERENTIAL_STRESS = "PRESSURE_DIFFERENTIAL_STRESS"
    ELECTROMAGNETIC_SURGE_EFFECTS = "ELECTROMAGNETIC_SURGE_EFFECTS"
    ATMOSPHERIC_ENTRY_HEAT = "ATMOSPHERIC_ENTRY_HEAT"


class ShipEngineSymbol(StrEnum):
    ENGINE_IMPULSE_DRIVE_I = "ENGINE_IMPULSE_DRIVE_I"
    ENGINE_ION_DRIVE_I = "ENGINE_ION_DRIVE_I"
    ENGINE_ION_DRIVE_II = "ENGINE_ION_DRIVE_II"
    ENGINE_HYPER_DRIVE_I = "ENGINE_HYPER_DRIVE_I"


class ShipFrameSymbol(StrEnum):
    FRAME_PROBE = "FRAME_PROBE"
    FRAME_DRONE = "FRAME_DRONE"
    FRAME_INTERCEPTOR = "FRAME_INTERCEPTOR"
    FRAME_RACER = "FRAME_RACER"
    FRAME_FIGHTER = "FRAME_FIGHTER"
    FRAME_FRIGATE = "FRAME_FRIGATE"
    FRAME_SHUTTLE = "FRAME_SHUTTLE"
    FRAME_EXPLORER = "FRAME_EXPLORER"
    FRAME_MINER = "FRAME_MINER"
    FRAME_LIGHT_FREIGHTER = "FRAME_LIGHT_FREIGHTER"
    FRAME_HEAVY_FREIGHTER = "FRAME_HEAVY_FREIGHTER"
    FRAME_TRANSPORT = "FRAME_TRANSPORT"
    FRAME_DESTROYER = "FRAME_DESTROYER"
    FRAME_CRUISER = "FRAME_CRUISER"
    FRAME_CARRIER = "FRAME_CARRIER"


class ShipModuleSymbol(StrEnum):
    MODULE_MINERAL_PROCESSOR_I = "MODULE_MINERAL_PROCESSOR_I"
    MODULE_GAS_PROCESSOR_I = "MODULE_GAS_PROCESSOR_I"
    MODULE_CARGO_HOLD_I = "MODULE_CARGO_HOLD_I"
    MODULE_CARGO_HOLD_II = "MODULE_CARGO_HOLD_II"
    MODULE_CARGO_HOLD_III = "MODULE_CARGO_HOLD_III"
    MODULE_CREW_QUARTERS_I = "MODULE_CREW_QUARTERS_I"
    MODULE_ENVOY_QUARTERS_I = "MODULE_ENVOY_QUARTERS_I"
    MODULE_PASSENGER_CABIN_I = "MODULE_PASSENGER_CABIN_I"
    MODULE_MICRO_REFINERY_I = "MODULE_MICRO_REFINERY_I"
    MODULE_ORE_REFINERY_I = "MODULE_ORE_REFINERY_I"
    MODULE_FUEL_REFINERY_I = "MODULE_FUEL_REFINERY_I"
    MODULE_SCIENCE_LAB_I = "MODULE_SCIENCE_LAB_I"
    MODULE_JUMP_DRIVE_I = "MODULE_JUMP_DRIVE_I"
    MODULE_JUMP_DRIVE_II = "MODULE_JUMP_DRIVE_II"
    MODULE_JUMP_DRIVE_III = "MODULE_JUMP_DRIVE_III"
    MODULE_WARP_DRIVE_I = "MODULE_WARP_DRIVE_I"
    MODULE_WARP_DRIVE_II = "MODULE_WARP_DRIVE_II"
    MODULE_WARP_DRIVE_III = "MODULE_WARP_DRIVE_III"
    MODULE_SHIELD_GENERATOR_I = "MODULE_SHIELD_GENERATOR_I"
    MODULE_SHIELD_GENERATOR_II = "MODULE_SHIELD_GENERATOR_II"


class ShipMountSymbol(StrEnum):
    MOUNT_GAS_SIPHON_I = "MOUNT_GAS_SIPHON_I"
    MOUNT_GAS_SIPHON_II = "MOUNT_GAS_SIPHON_II"
    MOUNT_GAS_SIPHON_III = "MOUNT_GAS_SIPHON_III"
    MOUNT_SURVEYOR_I = "MOUNT_SURVEYOR_I"
    MOUNT_SURVEYOR_II = "MOUNT_SURVEYOR_II"
    MOUNT_SURVEYOR_III = "MOUNT_SURVEYOR_III"
    MOUNT_SENSOR_ARRAY_I = "MOUNT_SENSOR_ARRAY_I"
    MOUNT_SENSOR_ARRAY_II = "MOUNT_SENSOR_ARRAY_II"
    MOUNT_SENSOR_ARRAY_III = "MOUNT_SENSOR_ARRAY_III"
    MOUNT_MINING_LASER_I = "MOUNT_MINING_LASER_I"
    MOUNT_MINING_LASER_II = "MOUNT_MINING_LASER_II"
    MOUNT_MINING_LASER_III = "MOUNT_MINING_LASER_III"
    MOUNT_LASER_CANNON_I = "MOUNT_LASER_CANNON_I"
    MOUNT_MISSILE_LAUNCHER_I = "MOUNT_MISSILE_LAUNCHER_I"
    MOUNT_TURRET_I = "MOUNT_TURRET_I"


class ShipNavStatus(StrEnum):
    IN_TRANSIT = "IN_TRANSIT"
    IN_ORBIT = "IN_ORBIT"
    DOCKED = "DOCKED"


class ShipNavFlightMode(StrEnum):
    DRIFT = "DRIFT"
    STEALTH = "STEALTH"
    CRUISE = "CRUISE"
    BURN = "BURN"


class ShipReactorSymbol(StrEnum):
    REACTOR_SOLAR_I = "REACTOR_SOLAR_I"
    REACTOR_FUSION_I = "REACTOR_FUSION_I"
    REACTOR_FISSION_I = "REACTOR_FISSION_I"
    REACTOR_CHEMICAL_I = "REACTOR_CHEMICAL_I"
    REACTOR_ANTIMATTER_I = "REACTOR_ANTIMATTER_I"


class ShipRole(StrEnum):
    FABRICATOR = "FABRICATOR"
    HARVESTER = "HARVESTER"
    HAULER = "HAULER"
    INTERCEPTOR = "INTERCEPTOR"
    EXCAVATOR = "EXCAVATOR"
    TRANSPORT = "TRANSPORT"
    REPAIR = "REPAIR"
    SURVEYOR = "SURVEYOR"
    COMMAND = "COMMAND"
    CARRIER = "CARRIER"
    PATROL = "PATROL"
    SATELLITE = "SATELLITE"
    EXPLORER = "EXPLORER"
    REFINERY = "REFINERY"


class ShipType(StrEnum):
    SHIP_PROBE = "SHIP_PROBE"
    SHIP_MINING_DRONE = "SHIP_MINING_DRONE"
    SHIP_SIPHON_DRONE = "SHIP_SIPHON_DRONE"
    SHIP_INTERCEPTOR = "SHIP_INTERCEPTOR"
    SHIP_LIGHT_HAULER = "SHIP_LIGHT_HAULER"
    SHIP_COMMAND_FRIGATE = "SHIP_COMMAND_FRIGATE"
    SHIP_EXPLORER = "SHIP_EXPLORER"
    SHIP_HEAVY_FREIGHTER = "SHIP_HEAVY_FREIGHTER"
    SHIP_LIGHT_SHUTTLE = "SHIP_LIGHT_SHUTTLE"
    SHIP_ORE_HOUND = "SHIP_ORE_HOUND"
    SHIP_REFINING_FREIGHTER = "SHIP_REFINING_FREIGHTER"
    SHIP_SURVEYOR = "SHIP_SURVEYOR"


class SupplyLevel(StrEnum):
    SCARCE = "SCARCE"
    LIMITED = "LIMITED"
    MODERATE = "MODERATE"
    HIGH = "HIGH"
    ABUNDANT = "ABUNDANT"


class SystemType(StrEnum):
    NEUTRON_STAR = "NEUTRON_STAR"
    RED_STAR = "RED_STAR"
    ORANGE_STAR = "ORANGE_STAR"
    BLUE_STAR = "BLUE_STAR"
    YOUNG_STAR = "YOUNG_STAR"
    WHITE_DWARF = "WHITE_DWARF"
    BLACK_HOLE = "BLACK_HOLE"
    HYPERGIANT = "HYPERGIANT"
    NEBULA = "NEBULA"
    UNSTABLE = "UNSTABLE"


class TradeSymbol(StrEnum):
    PRECIOUS_STONES = "PRECIOUS_STONES"
    QUARTZ_SAND = "QUARTZ_SAND"
    SILICON_CRYSTALS = "SILICON_CRYSTALS"
    AMMONIA_ICE = "AMMONIA_ICE"
    LIQUID_HYDROGEN = "LIQUID_HYDROGEN"
    LIQUID_NITROGEN = "LIQUID_NITROGEN"
    ICE_WATER = "ICE_WATER"
    EXOTIC_MATTER = "EXOTIC_MATTER"
    ADVANCED_CIRCUITRY = "ADVANCED_CIRCUITRY"
    GRAVITON_EMITTERS = "GRAVITON_EMITTERS"
    IRON = "IRON"
    IRON_ORE = "IRON_ORE"
    COPPER = "COPPER"
    COPPER_ORE = "COPPER_ORE"
    ALUMINUM = "ALUMINUM"
    ALUMINUM_ORE = "ALUMINUM_ORE"
    SILVER = "SILVER"
    SILVER_ORE = "SILVER_ORE"
    GOLD = "GOLD"
    GOLD_ORE = "GOLD_ORE"
    PLATINUM = "PLATINUM"
    PLATINUM_ORE = "PLATINUM_ORE"
    DIAMONDS = "DIAMONDS"
    URANITE = "URANITE"
    URANITE_ORE = "URANITE_ORE"
    MERITIUM = "MERITIUM"
    MERITIUM_ORE = "MERITIUM_ORE"
    HYDROCARBON = "HYDROCARBON"
    ANTIMATTER = "ANTIMATTER"
    FAB_MATS = "FAB_MATS"
    FERTILIZERS = "FERTILIZERS"
    FABRICS = "FABRICS"
    FOOD = "FOOD"
    JEWELRY = "JEWELRY"
    MACHINERY = "MACHINERY"
    FIREARMS = "FIREARMS"
    ASSAULT_RIFLES = "ASSAULT_RIFLES"
    MILITARY_EQUIPMENT = "MILITARY_EQUIPMENT"
    EXPLOSIVES = "EXPLOSIVES"
    LAB_INSTRUMENTS = "LAB_INSTRUMENTS"
    AMMUNITION = "AMMUNITION"
    ELECTRONICS = "ELECTRONICS"
    SHIP_PLATING = "SHIP_PLATING"
    SHIP_PARTS = "SHIP_PARTS"
    EQUIPMENT = "EQUIPMENT"
    FUEL = "FUEL"
    MEDICINE = "MEDICINE"
    DRUGS = "DRUGS"
    CLOTHING = "CLOTHING"
    MICROPROCESSORS = "MICROPROCESSORS"
    PLASTICS = "PLASTICS"
    POLYNUCLEOTIDES = "POLYNUCLEOTIDES"
    BIOCOMPOSITES = "BIOCOMPOSITES"
    QUANTUM_STABILIZERS = "QUANTUM_STABILIZERS"
    NANOBOTS = "NANOBOTS"
    AI_MAINFRAMES = "AI_MAINFRAMES"
    QUANTUM_DRIVES = "QUANTUM_DRIVES"
    ROBOTIC_DRONES = "ROBOTIC_DRONES"
    CYBER_IMPLANTS = "CYBER_IMPLANTS"
    GENE_THERAPEUTICS = "GENE_THERAPEUTICS"
    NEURAL_CHIPS = "NEURAL_CHIPS"
    MOOD_REGULATORS = "MOOD_REGULATORS"
    VIRAL_AGENTS = "VIRAL_AGENTS"
    MICRO_FUSION_GENERATORS = "MICRO_FUSION_GENERATORS"
    SUPERGRAINS = "SUPERGRAINS"
    LASER_RIFLES = "LASER_RIFLES"
    HOLOGRAPHICS = "HOLOGRAPHICS"
    SHIP_SALVAGE = "SHIP_SALVAGE"
    RELIC_TECH = "RELIC_TECH"
    NOVEL_LIFEFORMS = "NOVEL_LIFEFORMS"
    BOTANICAL_SPECIMENS = "BOTANICAL_SPECIMENS"
    CULTURAL_ARTIFACTS = "CULTURAL_ARTIFACTS"
    FRAME_PROBE = "FRAME_PROBE"
    FRAME_DRONE = "FRAME_DRONE"
    FRAME_INTERCEPTOR = "FRAME_INTERCEPTOR"
    FRAME_RACER = "FRAME_RACER"
    FRAME_FIGHTER = "FRAME_FIGHTER"
    FRAME_FRIGATE = "FRAME_FRIGATE"
    FRAME_SHUTTLE = "FRAME_SHUTTLE"
    FRAME_EXPLORER = "FRAME_EXPLORER"
    FRAME_MINER = "FRAME_MINER"
    FRAME_LIGHT_FREIGHTER = "FRAME_LIGHT_FREIGHTER"
    FRAME_HEAVY_FREIGHTER = "FRAME_HEAVY_FREIGHTER"
    FRAME_TRANSPORT = "FRAME_TRANSPORT"
    FRAME_DESTROYER = "FRAME_DESTROYER"
    FRAME_CRUISER = "FRAME_CRUISER"
    FRAME_CARRIER = "FRAME_CARRIER"
    REACTOR_SOLAR_I = "REACTOR_SOLAR_I"
    REACTOR_FUSION_I = "REACTOR_FUSION_I"
    REACTOR_FISSION_I = "REACTOR_FISSION_I"
    REACTOR_CHEMICAL_I = "REACTOR_CHEMICAL_I"
    REACTOR_ANTIMATTER_I = "REACTOR_ANTIMATTER_I"
    ENGINE_IMPULSE_DRIVE_I = "ENGINE_IMPULSE_DRIVE_I"
    ENGINE_ION_DRIVE_I = "ENGINE_ION_DRIVE_I"
    ENGINE_ION_DRIVE_II = "ENGINE_ION_DRIVE_II"
    ENGINE_HYPER_DRIVE_I = "ENGINE_HYPER_DRIVE_I"
    MODULE_MINERAL_PROCESSOR_I = "MODULE_MINERAL_PROCESSOR_I"
    MODULE_GAS_PROCESSOR_I = "MODULE_GAS_PROCESSOR_I"
    MODULE_CARGO_HOLD_I = "MODULE_CARGO_HOLD_I"
    MODULE_CARGO_HOLD_II = "MODULE_CARGO_HOLD_II"
    MODULE_CARGO_HOLD_III = "MODULE_CARGO_HOLD_III"
    MODULE_CREW_QUARTERS_I = "MODULE_CREW_QUARTERS_I"
    MODULE_ENVOY_QUARTERS_I = "MODULE_ENVOY_QUARTERS_I"
    MODULE_PASSENGER_CABIN_I = "MODULE_PASSENGER_CABIN_I"
    MODULE_MICRO_REFINERY_I = "MODULE_MICRO_REFINERY_I"
    MODULE_SCIENCE_LAB_I = "MODULE_SCIENCE_LAB_I"
    MODULE_JUMP_DRIVE_I = "MODULE_JUMP_DRIVE_I"
    MODULE_JUMP_DRIVE_II = "MODULE_JUMP_DRIVE_II"
    MODULE_JUMP_DRIVE_III = "MODULE_JUMP_DRIVE_III"
    MODULE_WARP_DRIVE_I = "MODULE_WARP_DRIVE_I"
    MODULE_WARP_DRIVE_II = "MODULE_WARP_DRIVE_II"
    MODULE_WARP_DRIVE_III = "MODULE_WARP_DRIVE_III"
    MODULE_SHIELD_GENERATOR_I = "MODULE_SHIELD_GENERATOR_I"
    MODULE_SHIELD_GENERATOR_II = "MODULE_SHIELD_GENERATOR_II"
    MODULE_ORE_REFINERY_I = "MODULE_ORE_REFINERY_I"
    MODULE_FUEL_REFINERY_I = "MODULE_FUEL_REFINERY_I"
    MOUNT_GAS_SIPHON_I = "MOUNT_GAS_SIPHON_I"
    MOUNT_GAS_SIPHON_II = "MOUNT_GAS_SIPHON_II"
    MOUNT_GAS_SIPHON_III = "MOUNT_GAS_SIPHON_III"
    MOUNT_SURVEYOR_I = "MOUNT_SURVEYOR_I"
    MOUNT_SURVEYOR_II = "MOUNT_SURVEYOR_II"
    MOUNT_SURVEYOR_III = "MOUNT_SURVEYOR_III"
    MOUNT_SENSOR_ARRAY_I = "MOUNT_SENSOR_ARRAY_I"
    MOUNT_SENSOR_ARRAY_II = "MOUNT_SENSOR_ARRAY_II"
    MOUNT_SENSOR_ARRAY_III = "MOUNT_SENSOR_ARRAY_III"
    MOUNT_MINING_LASER_I = "MOUNT_MINING_LASER_I"
    MOUNT_MINING_LASER_II = "MOUNT_MINING_LASER_II"
    MOUNT_MINING_LASER_III = "MOUNT_MINING_LASER_III"
    MOUNT_LASER_CANNON_I = "MOUNT_LASER_CANNON_I"
    MOUNT_MISSILE_LAUNCHER_I = "MOUNT_MISSILE_LAUNCHER_I"
    MOUNT_TURRET_I = "MOUNT_TURRET_I"
    SHIP_PROBE = "SHIP_PROBE"
    SHIP_MINING_DRONE = "SHIP_MINING_DRONE"
    SHIP_SIPHON_DRONE = "SHIP_SIPHON_DRONE"
    SHIP_INTERCEPTOR = "SHIP_INTERCEPTOR"
    SHIP_LIGHT_HAULER = "SHIP_LIGHT_HAULER"
    SHIP_COMMAND_FRIGATE = "SHIP_COMMAND_FRIGATE"
    SHIP_EXPLORER = "SHIP_EXPLORER"
    SHIP_HEAVY_FREIGHTER = "SHIP_HEAVY_FREIGHTER"
    SHIP_LIGHT_SHUTTLE = "SHIP_LIGHT_SHUTTLE"
    SHIP_ORE_HOUND = "SHIP_ORE_HOUND"
    SHIP_REFINING_FREIGHTER = "SHIP_REFINING_FREIGHTER"
    SHIP_SURVEYOR = "SHIP_SURVEYOR"


class WaypointModifierSymbol(StrEnum):
    STRIPPED = "STRIPPED"
    UNSTABLE = "UNSTABLE"
    RADIATION_LEAK = "RADIATION_LEAK"
    CRITICAL_LIMIT = "CRITICAL_LIMIT"
    CIVIL_UNREST = "CIVIL_UNREST"


class WaypointTraitSymbol(StrEnum):
    UNCHARTED = "UNCHARTED"
    UNDER_CONSTRUCTION = "UNDER_CONSTRUCTION"
    MARKETPLACE = "MARKETPLACE"
    SHIPYARD = "SHIPYARD"
    OUTPOST = "OUTPOST"
    SCATTERED_SETTLEMENTS = "SCATTERED_SETTLEMENTS"
    SPRAWLING_CITIES = "SPRAWLING_CITIES"
    MEGA_STRUCTURES = "MEGA_STRUCTURES"
    PIRATE_BASE = "PIRATE_BASE"
    OVERCROWDED = "OVERCROWDED"
    HIGH_TECH = "HIGH_TECH"
    CORRUPT = "CORRUPT"
    BUREAUCRATIC = "BUREAUCRATIC"
    TRADING_HUB = "TRADING_HUB"
    INDUSTRIAL = "INDUSTRIAL"
    BLACK_MARKET = "BLACK_MARKET"
    RESEARCH_FACILITY = "RESEARCH_FACILITY"
    MILITARY_BASE = "MILITARY_BASE"
    SURVEILLANCE_OUTPOST = "SURVEILLANCE_OUTPOST"
    EXPLORATION_OUTPOST = "EXPLORATION_OUTPOST"
    MINERAL_DEPOSITS = "MINERAL_DEPOSITS"
    COMMON_METAL_DEPOSITS = "COMMON_METAL_DEPOSITS"
    PRECIOUS_METAL_DEPOSITS = "PRECIOUS_METAL_DEPOSITS"
    RARE_METAL_DEPOSITS = "RARE_METAL_DEPOSITS"
    METHANE_POOLS = "METHANE_POOLS"
    ICE_CRYSTALS = "ICE_CRYSTALS"
    EXPLOSIVE_GASES = "EXPLOSIVE_GASES"
    STRONG_MAGNETOSPHERE = "STRONG_MAGNETOSPHERE"
    VIBRANT_AURORAS = "VIBRANT_AURORAS"
    SALT_FLATS = "SALT_FLATS"
    CANYONS = "CANYONS"
    PERPETUAL_DAYLIGHT = "PERPETUAL_DAYLIGHT"
    PERPETUAL_OVERCAST = "PERPETUAL_OVERCAST"
    DRY_SEABEDS = "DRY_SEABEDS"
    MAGMA_SEAS = "MAGMA_SEAS"
    SUPERVOLCANOES = "SUPERVOLCANOES"
    ASH_CLOUDS = "ASH_CLOUDS"
    VAST_RUINS = "VAST_RUINS"
    MUTATED_FLORA = "MUTATED_FLORA"
    TERRAFORMED = "TERRAFORMED"
    EXTREME_TEMPERATURES = "EXTREME_TEMPERATURES"
    EXTREME_PRESSURE = "EXTREME_PRESSURE"
    DIVERSE_LIFE = "DIVERSE_LIFE"
    SCARCE_LIFE = "SCARCE_LIFE"
    FOSSILS = "FOSSILS"
    WEAK_GRAVITY = "WEAK_GRAVITY"
    STRONG_GRAVITY = "STRONG_GRAVITY"
    CRUSHING_GRAVITY = "CRUSHING_GRAVITY"
    TOXIC_ATMOSPHERE = "TOXIC_ATMOSPHERE"
    CORROSIVE_ATMOSPHERE = "CORROSIVE_ATMOSPHERE"
    BREATHABLE_ATMOSPHERE = "BREATHABLE_ATMOSPHERE"
    THIN_ATMOSPHERE = "THIN_ATMOSPHERE"
    JOVIAN = "JOVIAN"
    ROCKY = "ROCKY"
    VOLCANIC = "VOLCANIC"
    FROZEN = "FROZEN"
    SWAMP = "SWAMP"
    BARREN = "BARREN"
    TEMPERATE = "TEMPERATE"
    JUNGLE = "JUNGLE"
    OCEAN = "OCEAN"
    RADIOACTIVE = "RADIOACTIVE"
    MICRO_GRAVITY_ANOMALIES = "MICRO_GRAVITY_ANOMALIES"
    DEBRIS_CLUSTER = "DEBRIS_CLUSTER"
    DEEP_CRATERS = "DEEP_CRATERS"
    SHALLOW_CRATERS = "SHALLOW_CRATERS"
    UNSTABLE_COMPOSITION = "UNSTABLE_COMPOSITION"
    HOLLOWED_INTERIOR = "HOLLOWED_INTERIOR"
    STRIPPED = "STRIPPED"


class WaypointType(StrEnum):
    PLANET = "PLANET"
    GAS_GIANT = "GAS_GIANT"
    MOON = "MOON"
    ORBITAL_STATION = "ORBITAL_STATION"
    JUMP_GATE = "JUMP_GATE"
    ASTEROID_FIELD = "ASTEROID_FIELD"
    ASTEROID = "ASTEROID"
    ENGINEERED_ASTEROID = "ENGINEERED_ASTEROID"
    ASTEROID_BASE = "ASTEROID_BASE"
    NEBULA = "NEBULA"
    DEBRIS_FIELD = "DEBRIS_FIELD"
    GRAVITY_WELL = "GRAVITY_WELL"
    ARTIFICIAL_GRAVITY_WELL = "ARTIFICIAL_GRAVITY_WELL"
    FUEL_STATION = "FUEL_STATION"


class Codes(Enum):
    # HTTP ApiError Codes
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    PAYMENT_REQUIRED = 402
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    PROXY_AUTHENTICATION_REQUIRED = 407
    REQUEST_TIMEOUT = 408
    CONFLICT = 409
    GONE = 410
    LENGTH_REQUIRED = 411
    PRECONDITION_FAILED = 412
    PAYLOAD_TOO_LARGE = 413
    URI_TOO_LONG = 414
    UNSUPPORTED_MEDIA_TYPE = 415
    RANGE_NOT_SATISFIABLE = 416
    EXPECTATION_FAILED = 417
    IM_A_TEAPOT = 418
    MISDIRECTED_REQUEST = 421
    UNPROCESSABLE_ENTITY = 422
    LOCKED = 423
    FAILED_DEPENDENCY = 424
    TOO_EARLY = 425
    UPGRADE_REQUIRED = 426
    PRECONDITION_REQUIRED = 428
    TOO_MANY_REQUESTS = 429
    REQUEST_HEADER_FIELDS_TOO_LARGE = 431
    UNAVAILABLE_FOR_LEGAL_REASONS = 451

    # class GeneralCodes(Enum):
    # General ApiError Codes
    COOLDOWN_CONFLICT_ERROR = 4000
    WAYPOINT_NO_ACCESS_ERROR = 4001

    # class AccountCodes(Enum):
    # Account ApiError Codes
    TOKEN_EMPTY_ERROR = 4100
    TOKEN_MISSING_SUBJECT_ERROR = 4101
    TOKEN_INVALID_SUBJECT_ERROR = 4102
    MISSING_TOKEN_REQUEST_ERROR = 4103
    INVALID_TOKEN_REQUEST_ERROR = 4104
    INVALID_TOKEN_SUBJECT_ERROR = 4105
    ACCOUNT_NOT_EXISTS_ERROR = 4106
    AGENT_NOT_EXISTS_ERROR = 4107
    ACCOUNT_HAS_NO_AGENT_ERROR = 4108
    REGISTER_AGENT_EXISTS_ERROR = 4109
    REGISTER_AGENT_SYMBOL_RESERVED_ERROR = 4110
    REGISTER_AGENT_CONFLICT_SYMBOL_ERROR = 4111

    # class ShipCodes(Enum):
    # Ship ApiError Codes
    NAVIGATE_IN_TRANSIT_ERROR = 4200
    NAVIGATE_INVALID_DESTINATION_ERROR = 4201
    NAVIGATE_OUTSIDE_SYSTEM_ERROR = 4202
    NAVIGATE_INSUFFICIENT_FUEL_ERROR = 4203
    NAVIGATE_SAME_DESTINATION_ERROR = 4204
    SHIP_EXTRACT_INVALID_WAYPOINT_ERROR = 4205
    SHIP_EXTRACT_PERMISSION_ERROR = 4206
    SHIP_JUMP_NO_SYSTEM_ERROR = 4207
    SHIP_JUMP_SAME_SYSTEM_ERROR = 4208
    SHIP_JUMP_MISSING_MODULE_ERROR = 4210
    SHIP_JUMP_NO_VALID_WAYPOINT_ERROR = 4211
    SHIP_JUMP_MISSING_ANTIMATTER_ERROR = 4212
    SHIP_IN_TRANSIT_ERROR = 4214
    SHIP_MISSING_SENSOR_ARRAYS_ERROR = 4215
    PURCHASE_SHIP_CREDITS_ERROR = 4216
    SHIP_CARGO_EXCEEDS_LIMIT_ERROR = 4217
    SHIP_CARGO_MISSING_ERROR = 4218
    SHIP_CARGO_UNIT_COUNT_ERROR = 4219
    SHIP_SURVEY_VERIFICATION_ERROR = 4220
    SHIP_SURVEY_EXPIRATION_ERROR = 4221
    SHIP_SURVEY_WAYPOINT_TYPE_ERROR = 4222
    SHIP_SURVEY_ORBIT_ERROR = 4223
    SHIP_SURVEY_EXHAUSTED_ERROR = 4224
    SHIP_REFUEL_DOCKED_ERROR = 4225
    SHIP_REFUEL_INVALID_WAYPOINT_ERROR = 4226
    SHIP_MISSING_MOUNTS_ERROR_4227 = 4227
    SHIP_CARGO_FULL_ERROR = 4228
    SHIP_JUMP_FROM_GATE_TO_GATE_ERROR = 4229
    WAYPOINT_CHARTED_ERROR = 4230
    SHIP_TRANSFER_SHIP_NOT_FOUND = 4231
    SHIP_TRANSFER_AGENT_CONFLICT = 4232
    SHIP_TRANSFER_SAME_SHIP_CONFLICT = 4233
    SHIP_TRANSFER_LOCATION_CONFLICT = 4234
    WARP_INSIDE_SYSTEM_ERROR = 4235
    SHIP_NOT_IN_ORBIT_ERROR = 4236
    SHIP_INVALID_REFINERY_GOOD_ERROR = 4237
    SHIP_INVALID_REFINERY_TYPE_ERROR = 4238
    SHIP_MISSING_REFINERY_ERROR = 4239
    SHIP_MISSING_SURVEYOR_ERROR = 4240
    SHIP_MISSING_WARP_DRIVE_ERROR = 4241
    SHIP_MISSING_MINERAL_PROCESSOR_ERROR = 4242
    SHIP_MISSING_MINING_LASERS_ERROR = 4243
    SHIP_NOT_DOCKED_ERROR = 4244
    PURCHASE_SHIP_NOT_PRESENT_ERROR = 4245
    SHIP_MOUNT_NO_SHIPYARD_ERROR = 4246
    SHIP_MISSING_MOUNT_ERROR = 4247
    SHIP_MOUNT_INSUFFICIENT_CREDITS_ERROR = 4248
    SHIP_MISSING_POWER_ERROR = 4249
    SHIP_MISSING_SLOTS_ERROR = 4250
    SHIP_MISSING_MOUNTS_ERROR_4251 = 4251
    SHIP_MISSING_CREW_ERROR = 4252
    SHIP_EXTRACT_DESTABILIZED_ERROR = 4253
    SHIP_JUMP_INVALID_ORIGIN_ERROR = 4254
    SHIP_JUMP_INVALID_WAYPOINT_ERROR = 4255
    SHIP_JUMP_ORIGIN_UNDER_CONSTRUCTION_ERROR = 4256
    SHIP_MISSING_GAS_PROCESSOR_ERROR = 4257
    SHIP_MISSING_GAS_SIPHONS_ERROR = 4258
    SHIP_SIPHON_INVALID_WAYPOINT_ERROR = 4259
    SHIP_SIPHON_PERMISSION_ERROR = 4260
    WAYPOINT_NO_YIELD_ERROR = 4261
    SHIP_JUMP_DESTINATION_UNDER_CONSTRUCTION_ERROR = 4262
    SHIP_SCRAP_FAILED_ERROR = 4263
    SHIP_REPAIR_FAILED_ERROR = 4264

    # class ContractCodes(Enum):
    # Contract ApiError Codes
    ACCEPT_CONTRACT_NOT_AUTHORIZED_ERROR = 4500
    ACCEPT_CONTRACT_CONFLICT_ERROR = 4501
    FULFILL_CONTRACT_DELIVERY_ERROR = 4502
    CONTRACT_DEADLINE_ERROR = 4503
    CONTRACT_FULFILLED_ERROR = 4504
    CONTRACT_NOT_ACCEPTED_ERROR = 4505
    CONTRACT_NOT_AUTHORIZED_ERROR = 4506
    SHIP_DELIVER_TERMS_ERROR = 4508
    SHIP_DELIVER_FULFILLED_ERROR = 4509
    SHIP_DELIVER_INVALID_LOCATION_ERROR = 4510
    EXISTING_CONTRACT_ERROR = 4511

    # class MarketCodes(Enum):
    # Market ApiError Codes
    MARKET_TRADE_INSUFFICIENT_CREDITS_ERROR = 4600
    MARKET_TRADE_NO_PURCHASE_ERROR = 4601
    MARKET_TRADE_NOT_SOLD_ERROR = 4602
    MARKET_NOT_FOUND_ERROR = 4603
    MARKET_TRADE_UNIT_LIMIT_ERROR = 4604

    # class FactionCodes(Enum):
    # Faction ApiError Codes
    WAYPOINT_NO_FACTION_ERROR = 4700

    # class ConstructionCodes(Enum):
    # Construction ApiError Codes
    CONSTRUCTION_MATERIAL_NOT_REQUIRED = 4800
    CONSTRUCTION_MATERIAL_FULFILLED = 4801
    SHIP_CONSTRUCTION_INVALID_LOCATION_ERROR = 4802
