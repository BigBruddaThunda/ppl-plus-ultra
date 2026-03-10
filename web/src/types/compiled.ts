// Compiled zip code types — output of scripts/middle-math/city_compiler.py

export interface CompiledOrderInfo {
  emoji: string;
  name: string;
  index: number;
  classical: string;
}

export interface CompiledAxisInfo {
  emoji: string;
  name: string;
  index: number;
  latin: string;
}

export interface CompiledTypeInfo {
  emoji: string;
  name: string;
  index: number;
  muscles: string[];
}

export interface CompiledColorInfo {
  emoji: string;
  name: string;
  index: number;
  tier: string;
  gold: boolean;
  polarity: "preparatory" | "expressive";
}

export interface CompiledOperator {
  emoji: string;
  name: string;
  house?: string;
}

export interface CompiledAddress {
  zip_emoji: string;
  zip_numeric: string;
  order: CompiledOrderInfo;
  axis: CompiledAxisInfo;
  type: CompiledTypeInfo;
  color: CompiledColorInfo;
  operator: CompiledOperator;
  deck: number;
  url: string;
}

export interface CompiledMaterial {
  name: string;
  hue: number;
  sat: number | string;
  warmth: number;
  texture?: string;
  shadow?: string;
}

export interface CompiledAtmosphere {
  name: string;
  brightness: number;
  hue_shift: number;
  sat_multiplier: number;
  warmth_modifier: number;
  typography?: string;
}

export interface CompiledArchitecture {
  D: number | string;
  column_ratio: number;
  intercolumniation: number;
  superposition: number;
  line_multiplier: number;
  material: CompiledMaterial;
  atmosphere?: CompiledAtmosphere;
  shadow?: {
    depth_multiplier: number;
    hue: number;
    saturation: number | string;
    character: string;
  };
}

export interface CompiledPaletteRegister {
  primary: string;
  secondary: string;
  background: string;
  surface: string;
  text: string;
  accent: string;
  border: string;
  type_accent?: string;
  operator_tint?: string;
}

export interface CompiledPalette {
  active_register: string;
  light_register: CompiledPaletteRegister;
  dark_register: CompiledPaletteRegister;
  color_wheel?: Record<string, unknown>;
}

export interface CompiledTypography {
  font_family?: string;
  font_character?: string;
  body_size?: string;
  display_size?: string;
  font_weight?: number;
  font_weight_body?: number;
  font_weight_display?: number;
  letter_spacing: string;
  line_height: number;
  density: number | string;
  tonal_register?: {
    name: string;
    character: string;
  };
}

export interface CompiledPersonality {
  house: Record<string, unknown>;
  neighborhood?: Record<string, unknown>;
  city_position?: {
    building: string;
    floor: string;
    wing: string;
    room: string;
  };
  difficulty_class?: number;
  cns_demand?: string;
}

export interface CompiledConnections {
  navigation: Record<string, string>;
  deck_siblings?: number;
  same_deck_zips?: number;
  junction_suggestions?: Array<{ zip: string; similarity: number }>;
  cosine_nearest_5?: Array<{ zip: string; similarity: number }>;
  cosine_farthest?: string;
  abacus_memberships?: Array<{ id: number; name: string; slug: string }>;
  abacus_membership?: Array<{ id: number; name: string; slug: string }>;
}

export interface CompiledMetadata {
  deck: number;
  deck_name: string;
  operator_default: CompiledOperator;
  block_sequence: string[];
  block_count: number;
  difficulty_max?: number;
  cns?: string;
  gold_eligible: boolean;
  weight_vector: number[];
  vector_magnitude: number;
}

export interface CompiledZip {
  address: CompiledAddress;
  architecture: CompiledArchitecture;
  palette: CompiledPalette;
  typography: CompiledTypography;
  personality: CompiledPersonality;
  connections: CompiledConnections;
  metadata: CompiledMetadata;
}

export interface CompiledDeck {
  deck: number;
  order: Omit<CompiledOrderInfo, "index">;
  axis: Omit<CompiledAxisInfo, "index">;
  room_count: number;
  room_zips: string[];
  architecture: Pick<CompiledArchitecture, "D" | "column_ratio" | "intercolumniation" | "material">;
  centroid: number[];
  centroid_magnitude: number;
}

export interface CompiledAbacus {
  id: number;
  name: string;
  slug: string;
  domain: string;
  description: string;
  axis_bias: string;
  working_count: number;
  bonus_count: number;
  total_zips: number;
  working_zips: string[];
  bonus_zips: string[];
  centroid: number[];
  centroid_magnitude: number;
}
