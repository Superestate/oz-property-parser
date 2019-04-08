#!/usr/bin/env python3

import pytest

import property_definitions_nsw

DISTRICT_CODES = [
    ('001', 'CESSNOCK'),
    ('002', 'DUNGOG'),
    ('003', 'GOSFORD'),
    ('004', 'LAKE MACQUARIE'),
    ('005', 'MAITLAND'),
    ('007', 'MUSWELLBROOK'),
    ('008', 'NEWCASTLE'),
    ('010', 'PORT STEPHENS'),
    ('011', 'UPPER HUNTER (Former)'),
    ('012', 'SINGLETON'),
    ('013', 'GREAT LAKES'),
    ('014', 'WYONG'),
    ('018', 'BEGA VALLEY'),
    ('020', 'BOMBALA'),
    ('021', 'BOOROWA'),
    ('022', 'YOUNG'),
    ('024', 'COOTAMUNDRA'),
    ('026', 'CROOKWELL'),
    ('028', 'YASS'),
    ('029', 'GOULBURN'),
    ('031', 'GUNNING'),
    ('034', 'COOMA-MONARO'),
    ('035', 'MULWAREE'),
    ('037', 'HARDEN'),
    ('039', 'QUEANBEYAN'),
    ('040', 'TALLAGANDA'),
    ('042', 'COWRA'),
    ('043', 'WEDDIN'),
    ('044', 'YARROWLUMLA'),
    ('050', 'ALBURY'),
    ('051', 'BERRIGAN'),
    ('052', 'CARRATHOOL'),
    ('053', 'CONARGO'),
    ('054', 'COOLAMON'),
    ('055', 'COROWA'),
    ('056', 'CULCAIRN'),
    ('057', 'DENILIQUIN'),
    ('058', 'GUNDAGAI'),
    ('059', 'HOLBROOK'),
    ('060', 'HUME'),
    ('061', 'JUNEE'),
    ('062', 'JERILDERIE'),
    ('065', 'LEETON'),
    ('066', 'LOCKHART'),
    ('068', 'MURRAY'),
    ('069', 'MURRUMBIDGEE'),
    ('070', 'NARRANDERA'),
    ('071', 'TUMBARUMBA'),
    ('072', 'TUMUT'),
    ('073', 'URANA'),
    ('074', 'GRIFFITH'),
    ('076', 'WAKOOL'),
    ('077', 'WINDOURAN'),
    ('081', 'THE HILLS SHIRE'),
    ('082', 'HORNSBY'),
    ('083', 'HUNTERS HILL'),
    ('084', 'KU-RING-GAI'),
    ('085', 'LANE COVE'),
    ('086', 'MANLY'),
    ('087', 'MOSMAN'),
    ('088', 'NORTH SYDNEY'),
    ('089', 'PARRAMATTA'),
    ('090', 'RYDE'),
    ('091', 'WARRINGAH'),
    ('092', 'WILLOUGHBY'),
    ('093', 'PITTWATER'),
    ('097', 'EUROBODALLA'),
    ('098', 'KIAMA'),
    ('100', 'SHELLHARBOUR'),
    ('101', 'SHOALHAVEN'),
    ('102', 'WINGECARRIBEE'),
    ('103', 'WOLLONGONG'),
    ('108', 'BATHURST'),
    ('109', 'CABONNE'),
    ('112', 'WARRUMBUNGLE (Former)'),
    ('114', 'DUBBO'),
    ('116', 'PARKES'),
    ('117', 'FORBES'),
    ('118', 'BLAYNEY'),
    ('120', 'MUDGEE'),
    ('123', 'OBERON'),
    ('124', 'ORANGE'),
    ('127', 'RYLSTONE'),
    ('129', 'EVANS'),
    ('130', 'WELLINGTON'),
    ('134', 'ASHFIELD'),
    ('135', 'AUBURN'),
    ('136', 'BANKSTOWN'),
    ('137', 'BURWOOD'),
    ('138', 'CANTERBURY'),
    ('139', 'CANADA BAY'),
    ('140', 'HURSTVILLE'),
    ('141', 'KOGARAH'),
    ('142', 'ROCKDALE'),
    ('143', 'STRATHFIELD'),
    ('144', 'SUTHERLAND'),
    ('148', 'BALLINA'),
    ('149', 'BELLINGEN'),
    ('150', 'BYRON'),
    ('151', 'RICHMOND VALLEY'),
    ('152', 'COFFS HARBOUR'),
    ('153', 'COPMANHURST'),
    ('154', 'GRAFTON'),
    ('157', 'KEMPSEY'),
    ('158', 'KYOGLE'),
    ('159', 'LISMORE'),
    ('160', 'MACLEAN'),
    ('162', 'GREATER TAREE'),
    ('164', 'NAMBUCCA'),
    ('165', 'NYMBOIDA'),
    ('171', 'TWEED'),
    ('172', 'PRISTINE WATERS'),
    ('180', 'BARRABA'),
    ('181', 'BINGARA'),
    ('185', 'DUMARESQ'),
    ('186', 'GLEN INNES'),
    ('187', 'GUNNEDAH'),
    ('188', 'INVERELL'),
    ('191', 'MANILLA'),
    ('192', 'MOREE PLAINS'),
    ('194', 'NUNDLE'),
    ('195', 'PARRY'),
    ('197', 'QUIRINDI'),
    ('199', 'URALLA'),
    ('203', 'BOTANY BAY'),
    ('204', 'DRUMMOYNE'),
    ('205', 'LEICHHARDT'),
    ('206', 'MARRICKVILLE'),
    ('207', 'RANDWICK'),
    ('208', 'SYDNEY'),
    ('209', 'WAVERLEY'),
    ('210', 'WOOLLAHRA'),
    ('211', 'SOUTH SYDNEY'),
    ('214', 'BLACKTOWN'),
    ('216', 'BLUE MOUNTAINS'),
    ('217', 'CAMDEN'),
    ('218', 'CAMPBELLTOWN'),
    ('219', 'HAWKESBURY'),
    ('220', 'FAIRFIELD'),
    ('221', 'HOLROYD'),
    ('222', 'LITHGOW'),
    ('223', 'LIVERPOOL'),
    ('224', 'PENRITH'),
    ('226', 'WOLLONDILLY'),
    ('230', 'BALRANALD'),
    ('231', 'BLAND'),
    ('232', 'BOGAN'),
    ('233', 'BREWARRINA'),
    ('234', 'BROKEN HILL'),
    ('235', 'CENTRAL DARLING'),
    ('236', 'COBAR'),
    ('237', 'COONABARABRAN'),
    ('238', 'COONAMBLE'),
    ('239', 'BOURKE'),
    ('240', 'GILGANDRA'),
    ('241', 'GLOUCESTER'),
    ('242', 'GUYRA'),
    ('243', 'HAY'),
    ('244', 'LACHLAN'),
    ('245', 'MERRIWA'),
    ('246', 'MURRURUNDI'),
    ('247', 'NARRABRI'),
    ('248', 'SEVERN'),
    ('249', 'SNOWY RIVER'),
    ('250', 'TENTERFIELD'),
    ('251', 'NARROMINE'),
    ('252', 'WALCHA'),
    ('253', 'WALGETT'),
    ('254', 'WARREN'),
    ('255', 'WENTWORTH'),
    ('256', 'YALLAROI'),
    ('300', 'GWYDIR'),
    ('301', 'LIVERPOOL PLAINS'),
    ('302', 'GLEN INNES SEVERN'),
    ('303', 'CLARENCE VALLEY'),
    ('511', 'UPPER HUNTER'),
    ('526', 'UPPER LACHLAN'),
    ('528', 'YASS VALLEY'),
    ('529', 'GOULBURN MULWAREE'),
    ('537', 'WARRUMBUNGLE'),
    ('538', 'TEMORA'),
    ('539', 'QUEANBEYAN CITY'),
    ('540', 'PALERANG'),
    ('560', 'GREATER HUME'),
    ('575', 'WAGGA WAGGA'),
    ('608', 'BATHURST REGIONAL'),
    ('620', 'MID WESTERN REGIONAL'),
    ('623', 'OBERON (Former)'),
    ('656', 'PORT MACQUARIE-HASTINGS'),
    ('666', 'TAMWORTH REGIONAL'),
    ('672', 'COFFS HARBOUR (PW)'),
    ('678', 'ARMIDALE DUMARESQ'),
    ('695', 'LIVERPOOL PLAINS (Former)'),
    ('698', 'TAMWORTH'),
    ('708', 'CITY OF SYDNEY'),
    ('722', 'LITHGOW (Former)'),
    ('902', 'UNINCORPORATED AREA'),
    ('903', 'UNINCORPORATED SYDNEY'),
    ('905', 'SYDNEY (Former)'),
    ('911', 'SYDNEY (Former)'),
    ('INVALID_CODE', 'N/A')
]
@pytest.mark.parametrize('district_code, expected_district', DISTRICT_CODES)
def test_get_district_from_code(district_code, expected_district):
    assert property_definitions_nsw.get_district_from_code(district_code) == expected_district


ZONE_CODES_OLD = [
    ('A', 'Residential'),
    ('B', 'Business'),
    ('C', 'Sydney Commercial / Business'),
    ('D', '10(a) Sustainable Mixed Use Development'),
    ('E', 'Employment'),
    ('I', 'Industrial'),
    ('M', '9(a)(Mixed Residential / Business)'),
    ('N', 'National Parks'),
    ('O', 'Open Space'),
    ('P', 'Protection'),
    ('R', 'Non-Urban'),
    ('S', 'Special Uses'),
    ('T', 'North Sydney Commercial / Business'),
    ('U', 'Community Uses'),
    ('V', 'Comprehensive Centre'),
    ('W', 'Reserve Open Space'),
    ('X', 'Reserved Roads'),
    ('Y', 'Reserved Special Uses'),
    ('Z', 'Undetermined or Village'),
    ('INVALID_CODE', 'N/A')
]
@pytest.mark.parametrize('zone_code, expected_zone', ZONE_CODES_OLD)
def test_get_zone_from_old_code(zone_code, expected_zone):
    assert property_definitions_nsw.get_zone_from_old_code(zone_code) == expected_zone


ZONE_CODES_NEW = [
    ('RU1', 'Primary Production'),
    ('RU2', 'Rural Landscape'),
    ('RU3', 'Forestry'),
    ('RU4', 'Rural Small Holdings'),
    ('RU5', 'Village'),
    ('RU6', 'Transition'),
    ('R1', 'General Residential'),
    ('R2', 'Low Density Residential'),
    ('R3', 'Medium Density Residential'),
    ('R4', 'High Density Residential'),
    ('R5', 'Large Lot Residential'),
    ('B1', 'Neighbourhood Centre'),
    ('B2', 'Local Centre'),
    ('B3', 'Commercial Core'),
    ('B4', 'Mixed Use'),
    ('B5', 'Business Development'),
    ('B6', 'Enterprise Corridor'),
    ('B7', 'Business Park'),
    ('IN1', 'General Industrial'),
    ('IN2', 'Light Industrial'),
    ('IN3', 'Heavy Industrial'),
    ('IN4', 'Working Waterfront'),
    ('SP1', 'Special Activities'),
    ('SP2', 'Infrastructure'),
    ('SP3', 'Tourist'),
    ('RE1', 'Public Recreation'),
    ('RE2', 'Private Recreation'),
    ('E1', 'National Parks and Nature Reserves'),
    ('E2', 'Environmental Conservation'),
    ('E3', 'Environmental Management'),
    ('E4', 'Environmental Living'),
    ('W1', 'Natural Waterways'),
    ('W2', 'Recreational Waterways'),
    ('W3', 'Working Waterways'),
    ('INVALID_CODE', 'N/A')
]
@pytest.mark.parametrize('zone_code, expected_zone', ZONE_CODES_NEW)
def test_get_zone_from_old_code(zone_code, expected_zone):
    assert property_definitions_nsw.get_zone_from_new_code(zone_code) == expected_zone


ZONE_TYPE_NEW = [
    ('RU1', property_definitions_nsw.ZoneType.RURAL),
    ('RU2', property_definitions_nsw.ZoneType.RURAL),
    ('RU3', property_definitions_nsw.ZoneType.RURAL),
    ('RU4', property_definitions_nsw.ZoneType.RURAL),
    ('RU5', property_definitions_nsw.ZoneType.RURAL),
    ('RU6', property_definitions_nsw.ZoneType.RURAL),
    ('R1', property_definitions_nsw.ZoneType.RESIDENTIAL),
    ('R2', property_definitions_nsw.ZoneType.RESIDENTIAL),
    ('R3', property_definitions_nsw.ZoneType.RESIDENTIAL),
    ('R4', property_definitions_nsw.ZoneType.RESIDENTIAL),
    ('R5', property_definitions_nsw.ZoneType.RESIDENTIAL),
    ('B1', property_definitions_nsw.ZoneType.BUSINESS),
    ('B2', property_definitions_nsw.ZoneType.BUSINESS),
    ('B3', property_definitions_nsw.ZoneType.BUSINESS),
    ('B4', property_definitions_nsw.ZoneType.BUSINESS),
    ('B5', property_definitions_nsw.ZoneType.BUSINESS),
    ('B6', property_definitions_nsw.ZoneType.BUSINESS),
    ('B7', property_definitions_nsw.ZoneType.BUSINESS),
    ('IN1', property_definitions_nsw.ZoneType.INDUSTRIAL),
    ('IN2', property_definitions_nsw.ZoneType.INDUSTRIAL),
    ('IN3', property_definitions_nsw.ZoneType.INDUSTRIAL),
    ('IN4', property_definitions_nsw.ZoneType.INDUSTRIAL),
    ('SP1', property_definitions_nsw.ZoneType.SPECIAL_PURPOSE),
    ('SP2', property_definitions_nsw.ZoneType.SPECIAL_PURPOSE),
    ('SP3', property_definitions_nsw.ZoneType.SPECIAL_PURPOSE),
    ('RE1', property_definitions_nsw.ZoneType.RECREATION),
    ('RE2', property_definitions_nsw.ZoneType.RECREATION),
    ('E1', property_definitions_nsw.ZoneType.ENVIRONMENT_PROTECTION),
    ('E2', property_definitions_nsw.ZoneType.ENVIRONMENT_PROTECTION),
    ('E3', property_definitions_nsw.ZoneType.ENVIRONMENT_PROTECTION),
    ('E4', property_definitions_nsw.ZoneType.ENVIRONMENT_PROTECTION),
    ('W1', property_definitions_nsw.ZoneType.WATERWAY),
    ('W2', property_definitions_nsw.ZoneType.WATERWAY),
    ('W3', property_definitions_nsw.ZoneType.WATERWAY),
]
@pytest.mark.parametrize('zone_code, expected_zone_type', ZONE_TYPE_NEW)
def test_get_zone_from_old_code(zone_code, expected_zone_type):
    assert property_definitions_nsw.get_type_from_new_zone_code(zone_code) == expected_zone_type.value
