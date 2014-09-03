from __future__ import absolute_import, division, print_function, unicode_literals

# astropy/units/format/generic_parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\x06\x88\x92t\x1d[(\x7f\xb5\t\xa0\xbd\xaamgF'

_lr_action_items = {'CARET':([17,18,34,40,],[35,35,35,35,]),'SOLIDUS':([0,3,4,5,7,8,12,14,15,17,18,19,21,22,25,26,31,39,44,45,46,47,50,51,52,54,55,56,61,62,63,64,65,],[1,-25,-9,1,1,-23,-24,-13,-11,-16,-29,-12,-45,-44,-9,1,-22,-17,-28,-8,-26,-21,-14,-18,-43,-19,-27,-30,-47,-15,-20,1,-31,]),'STAR':([3,8,12,18,44,46,55,56,61,65,],[-25,29,-24,-29,-28,-26,-27,-30,-47,-31,]),'DOUBLE_STAR':([17,18,34,40,],[37,37,37,37,]),'PERIOD':([3,8,12,18,44,46,55,56,61,65,],[-25,30,-24,-29,-28,-26,-27,-30,-47,-31,]),'SQRT':([0,1,3,6,7,8,12,13,14,15,17,18,19,21,22,23,28,29,30,32,39,44,46,50,51,52,54,55,56,61,62,63,65,],[20,-40,-25,20,20,20,-24,20,-13,-11,-16,-29,-12,-45,-44,20,20,-38,-39,20,-17,-28,-26,-14,-18,-43,-19,-27,-30,-47,-15,-20,-31,]),'SIGN':([0,1,17,18,34,35,36,37,40,41,43,49,53,66,],[16,-40,38,16,38,-42,16,-41,38,16,16,16,16,16,]),'OPEN_PAREN':([0,1,3,6,7,8,11,12,13,14,15,17,18,19,20,21,22,23,28,29,30,32,35,36,37,39,41,44,46,49,50,51,52,53,54,55,56,61,62,63,65,],[6,-40,-25,6,6,6,32,-24,6,-13,-11,-16,43,-12,-46,-45,-44,6,6,-38,-39,6,-42,43,-41,-17,43,-28,-26,43,-14,-18,-43,43,-19,-27,-30,-47,-15,-20,-31,]),'UINT':([0,1,2,14,16,17,18,21,22,35,36,37,38,41,42,43,49,53,59,66,67,],[17,-40,22,34,-36,40,-37,-45,-44,-42,-37,-41,52,-37,56,-37,-37,-37,64,-37,68,]),'CLOSE_PAREN':([3,8,12,18,21,24,31,44,46,47,48,55,56,57,58,60,61,64,65,68,],[-25,-23,-24,-29,-45,46,-22,-28,-26,-21,61,-27,-30,-34,-33,65,-47,-32,-31,-35,]),'$end':([3,4,5,7,8,9,10,12,14,15,17,18,19,21,22,25,26,27,31,33,39,44,45,46,47,50,51,52,54,55,56,61,62,63,65,],[-25,-1,-3,-7,-23,0,-5,-24,-13,-11,-16,-29,-12,-45,-44,-2,-4,-6,-22,-10,-17,-28,-8,-26,-21,-14,-18,-43,-19,-27,-30,-47,-15,-20,-31,]),'UNIT':([0,1,3,6,7,8,12,13,14,15,17,18,19,21,22,23,28,29,30,32,39,44,46,50,51,52,54,55,56,61,62,63,65,],[18,-40,-25,18,18,18,-24,18,-13,-11,-16,-29,-12,-45,-44,18,18,-38,-39,18,-17,-28,-26,-14,-18,-43,-19,-27,-30,-47,-15,-20,-31,]),'UFLOAT':([0,2,16,43,59,],[-37,21,-36,-37,21,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
    for _x,_y in zip(_v[0],_v[1]):
        if not _x in _lr_action:  _lr_action[_x] = { }
        _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'function':([0,6,7,8,13,23,28,32,],[12,12,12,12,12,12,12,12,]),'division':([0,5,7,26,64,],[13,23,13,23,66,]),'product':([8,],[28,]),'frac':([43,],[57,]),'factor_int':([0,],[19,]),'power':([17,18,34,40,],[36,41,49,53,]),'unit_with_power':([0,6,7,8,13,23,28,32,],[3,3,3,3,3,3,3,3,]),'signed_float':([0,43,],[14,58,]),'product_of_units':([0,6,7,8,23,28,],[4,24,25,31,45,47,]),'factor_float':([0,],[15,]),'sign':([0,18,36,41,43,49,53,66,],[2,42,42,42,59,42,42,67,]),'signed_int':([17,34,40,],[39,50,54,]),'division_product_of_units':([0,7,],[5,26,]),'factor':([0,],[7,]),'unit_expression':([0,6,7,8,13,23,28,32,],[8,8,8,8,33,8,8,48,]),'numeric_power':([18,36,41,49,53,],[44,51,55,62,63,]),'main':([0,],[9,]),'paren_expr':([43,],[60,]),'inverse_unit':([0,7,],[10,27,]),'function_name':([0,6,7,8,13,23,28,32,],[11,11,11,11,11,11,11,11,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
    for _x,_y in zip(_v[0],_v[1]):
        if not _x in _lr_goto: _lr_goto[_x] = { }
        _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> main","S'",1,None,None,None),
  ('main -> product_of_units','main',1,'p_main','astropy/units/format/generic.py',124),
  ('main -> factor product_of_units','main',2,'p_main','astropy/units/format/generic.py',125),
  ('main -> division_product_of_units','main',1,'p_main','astropy/units/format/generic.py',126),
  ('main -> factor division_product_of_units','main',2,'p_main','astropy/units/format/generic.py',127),
  ('main -> inverse_unit','main',1,'p_main','astropy/units/format/generic.py',128),
  ('main -> factor inverse_unit','main',2,'p_main','astropy/units/format/generic.py',129),
  ('main -> factor','main',1,'p_main','astropy/units/format/generic.py',130),
  ('division_product_of_units -> division_product_of_units division product_of_units','division_product_of_units',3,'p_division_product_of_units','astropy/units/format/generic.py',140),
  ('division_product_of_units -> product_of_units','division_product_of_units',1,'p_division_product_of_units','astropy/units/format/generic.py',141),
  ('inverse_unit -> division unit_expression','inverse_unit',2,'p_inverse_unit','astropy/units/format/generic.py',151),
  ('factor -> factor_float','factor',1,'p_factor','astropy/units/format/generic.py',157),
  ('factor -> factor_int','factor',1,'p_factor','astropy/units/format/generic.py',158),
  ('factor_float -> signed_float','factor_float',1,'p_factor_float','astropy/units/format/generic.py',164),
  ('factor_float -> signed_float UINT signed_int','factor_float',3,'p_factor_float','astropy/units/format/generic.py',165),
  ('factor_float -> signed_float UINT power numeric_power','factor_float',4,'p_factor_float','astropy/units/format/generic.py',166),
  ('factor_int -> UINT','factor_int',1,'p_factor_int','astropy/units/format/generic.py',177),
  ('factor_int -> UINT signed_int','factor_int',2,'p_factor_int','astropy/units/format/generic.py',178),
  ('factor_int -> UINT power numeric_power','factor_int',3,'p_factor_int','astropy/units/format/generic.py',179),
  ('factor_int -> UINT UINT signed_int','factor_int',3,'p_factor_int','astropy/units/format/generic.py',180),
  ('factor_int -> UINT UINT power numeric_power','factor_int',4,'p_factor_int','astropy/units/format/generic.py',181),
  ('product_of_units -> unit_expression product product_of_units','product_of_units',3,'p_product_of_units','astropy/units/format/generic.py',197),
  ('product_of_units -> unit_expression product_of_units','product_of_units',2,'p_product_of_units','astropy/units/format/generic.py',198),
  ('product_of_units -> unit_expression','product_of_units',1,'p_product_of_units','astropy/units/format/generic.py',199),
  ('unit_expression -> function','unit_expression',1,'p_unit_expression','astropy/units/format/generic.py',210),
  ('unit_expression -> unit_with_power','unit_expression',1,'p_unit_expression','astropy/units/format/generic.py',211),
  ('unit_expression -> OPEN_PAREN product_of_units CLOSE_PAREN','unit_expression',3,'p_unit_expression','astropy/units/format/generic.py',212),
  ('unit_with_power -> UNIT power numeric_power','unit_with_power',3,'p_unit_with_power','astropy/units/format/generic.py',221),
  ('unit_with_power -> UNIT numeric_power','unit_with_power',2,'p_unit_with_power','astropy/units/format/generic.py',222),
  ('unit_with_power -> UNIT','unit_with_power',1,'p_unit_with_power','astropy/units/format/generic.py',223),
  ('numeric_power -> sign UINT','numeric_power',2,'p_numeric_power','astropy/units/format/generic.py',234),
  ('numeric_power -> OPEN_PAREN paren_expr CLOSE_PAREN','numeric_power',3,'p_numeric_power','astropy/units/format/generic.py',235),
  ('paren_expr -> sign UINT','paren_expr',2,'p_paren_expr','astropy/units/format/generic.py',244),
  ('paren_expr -> signed_float','paren_expr',1,'p_paren_expr','astropy/units/format/generic.py',245),
  ('paren_expr -> frac','paren_expr',1,'p_paren_expr','astropy/units/format/generic.py',246),
  ('frac -> sign UINT division sign UINT','frac',5,'p_frac','astropy/units/format/generic.py',255),
  ('sign -> SIGN','sign',1,'p_sign','astropy/units/format/generic.py',261),
  ('sign -> <empty>','sign',0,'p_sign','astropy/units/format/generic.py',262),
  ('product -> STAR','product',1,'p_product','astropy/units/format/generic.py',271),
  ('product -> PERIOD','product',1,'p_product','astropy/units/format/generic.py',272),
  ('division -> SOLIDUS','division',1,'p_division','astropy/units/format/generic.py',278),
  ('power -> DOUBLE_STAR','power',1,'p_power','astropy/units/format/generic.py',284),
  ('power -> CARET','power',1,'p_power','astropy/units/format/generic.py',285),
  ('signed_int -> SIGN UINT','signed_int',2,'p_signed_int','astropy/units/format/generic.py',291),
  ('signed_float -> sign UINT','signed_float',2,'p_signed_float','astropy/units/format/generic.py',297),
  ('signed_float -> sign UFLOAT','signed_float',2,'p_signed_float','astropy/units/format/generic.py',298),
  ('function_name -> SQRT','function_name',1,'p_function_name','astropy/units/format/generic.py',304),
  ('function -> function_name OPEN_PAREN unit_expression CLOSE_PAREN','function',4,'p_function','astropy/units/format/generic.py',310),
]