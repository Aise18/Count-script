import csv
import pandas as pd
import datetime

#current_date_map = datetime.datetime.now().strftime("%d%m%Y")
#file_path = f"//mcebucfnpp01/SharedData/GBS/MD/UK_CMF_REPORTS/MacroSpecSheets/MAP vs. Cost Price Daily Report {current_date_map}.csv"
#results51 = pd.read_csv(file_path)
results51 = pd.read_csv(r"//sharedrive_path/sharedrive_path/sharedrive_path_folder/sharedrive_path_folder/file_name.csv")
print(len(results51))
results1 = pd.read_csv(r"//sharedrive_path/sharedrive_path/sharedrive_path_folder/sharedrive_path_folder/file_name.csv")
print(len(results1))
results2 = pd.read_csv(r"//sharedrive_path/sharedrive_path/sharedrive_path_folder//sharedrive_path_folderfile_name.csv", encoding='ANSI')
print(len(results2))
results41 = pd.read_csv(r"//sharedrive_path/sharedrive_path/sharedrive_path_folder/sharedrive_path_folder/file_name.csv", encoding='latin-1', dtype=str, low_memory=False) 
print(len(results41))
r


header = ['REPORT_NAME', 'COUNT', 'DATEE', 'BUSINESS_UNIT', 'EMAIL', 'TEAM', 'VIEW', 'SUBJECT', 'REPORT_PATH']
current_date = datetime.datetime.now().strftime('%d-%b-%Y')

data = [
['MAP vs. Cost Price Daily Report', (len(results51)), current_date, 'UK', 'sam.butler@molsoncoors.com', 'MMD', 'VW_208_UK', 'MAP vs. Cost Price Daily Report', r'\\cblburfnp02\workgroup11\Logistics\MATERIAL MASTER\Code Master Files\MAP vs. Cost Price Daily Report'], 
['TT_FORM_SETUP', (len(results41)), current_date, 'UK', 'MaterialMasterData.UK@molsoncoors.com', 'MMD', 'VW_9999_TTFORM_UK', 'TT_FORM_SETUP', r'\\cblburfnp02\WORKGROUP11\Logistics\MATERIAL MASTER\Code Master Files\SQL'], 
['058_MSKU_VOLUME_CHECK', (len(results1)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_MSKU_VOL_CHECK', 'MD_MM_US_DL_058_MSKU_VOLUME_CHECK', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT058_MSKU_VOLUME_CHECK\058_MSKU_VOLUME_CHECK.csv'], 
['001_SOFT_DISCONTINUATION', (len(results2)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['CONTRACT_PIR_MATL_MASTER_ALT_UOM', (len(results3)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['CONTRACT_PIR_MATL_MASTER_PURC_GRP', (len(results4)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['CONTRACT_PIR_MATL_MASTER_ORD_PRICE_UNIT', (len(results5)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['Missing_charac_pivot', (len(results6)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['005_Backflush Indicator Audit', (len(results7)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_REPORT_BACKFLUSH_INDICATOR', 'MD_MM_US_DL_005_Backflush_Indicator_Audit', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\005_Backflush Indicator Audit\005_Backflush Indicator Audit.csv'], 
['CONTRACT_MM_PDT_GRPT', (len(results8)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['007_Wrong Costing Relevancy on BOM Components', (len(results9)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_BOM_COSTING_RELEVANCY', 'MD_MM_US_DL_007_Wrong_Costing_Relevancy_on_BOM_Components', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\007_Wrong Costing Relevancy on BOM Components\007_Wrong Costing Relevancy on BOM Components.csv'], 
['UPCs', (len(results10)), current_date, 'US', 'dlgbsmaterialteamus@millercoors.com, Heidi.Brungardt@millercoors.com (2 emails)', 'MMD', 'VW_PRICE_UPCSABV', 'All UPCs', r'\\mbsus238\trfshare\Master Data\Data Cleansing\Audit Reports\UPCs.csv'], 
['008_WIP Batch management audit', (len(results11)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_WIP_Batch_management', 'MD_MM_US_DL_008_WIP_Batch_management_audit', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\008_WIP Batch management audit\008_WIP Batch management audit.csv'], 
['009_PROFIT_CENTER_AUDIT', (len(results12)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'DM_MAT_CS_PRFT_CNTR_AUD2', 'MD_MM_US_DL_009_Profit_Center_Audit', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT009_PROFIT_CENTER_AUDIT\009_PROFIT_CENTER_AUDIT.csv'], 
['MSKU_OSKU_SQL_CHARS_AS_FIELD', (len(results13)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['MTRL_SQL_CHAR_ZPCKCAN', (len(results14)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['MATL_MSKUOSKU_MVKE', (len(results15)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['MATL_MSKUOSKU_MARC', (len(results16)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'],
['Proficy_Report', (len(results17)), current_date, 'UK', 'bpeftduk@molsoncoors.com, MaterialMasterData.UK@molsoncoors.com', 'MMD', 'VW_PROFICY_REPORT', 'Proficy_Report', r'\\Cblburfnp02\workgroup11\Logistics\MATERIAL MASTER\Code Master Files\Proficy_Report.csv'],
['MATL_OSKUOSKU_MARAMVKE', (len(results18)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['MATL_MSKUMSKU_MARAMVKE', (len(results19)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['BASE_MSKU_AUDIT', (len(results20)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['011_ZMSK AUOM PLANT X MATERIAL WITH PALLET QTY', (len(results22)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['012_ZWIP MATERIALS PROCUREMENT E WITH NO BOM', (len(results23)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['FINANCE WIP RECIPES', (len(results24)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['FINANCE MSKU RECIPES', (len(results25)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['072_BOM_VOLUME_CHECK_ZPCK', (len(results26)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com, CSCMaterialsPlanning@millercoors.com (2 emails)', 'MMD', 'VW_BOM_VOLUME_CHECK_ZPCK', 'MD_MM_US_DL_072_BOM_VOLUME_CHECK_ZPCK', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\072_BOM_VOLUME_CHECK_ZPCK\072_BOM_VOLUME_CHECK_ZPCK.csv'], 
['018_BOM_VOLUME_CHECK_ZWIP', (len(results27)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_BOM_VOLUME_CHECK_ZWIP', 'MD_MM_US_DL_018_BOM_VOLUME_CHECK_ZWIP', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\018_BOM_VOLUME_CHECK_ZWIP\018_BOM_VOLUME_CHECK_ZWIP.csv'], 
['Brand - Multiple Abrvs Per Brand Code', (len(results28)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['020_Direct-WIP Missing Sales or Storage View', (len(results29)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['Brand - Multiple Codes Per Brand Abrv', (len(results30)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['Inv_MSKU_WhseStock', (len(results31)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['022_Material - Price Unit Not Equal To 1000', (len(results32)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_MCS_705_MC_MBEW', 'MD_MM_US_DL_022_Material_Price_Unit_Not_Equal_To_1000', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\022_Material - Price Unit Not Equal To 1000\022_Material - Price Unit Not Equal To 1000.csv'], 
['023_ZRAW Wrong Batch Management', (len(results33)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_WRONG_BATCH_MNGMT_ZRAW', 'MD_MM_US_DL_023_ZRAW_Wrong_Batch_Management', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\023_ZRAW Wrong Batch Management\023_ZRAW Wrong Batch Management.csv'], 
['INFOSHEET_PRODUCTION', (len(results34)), current_date, 'US', 'dlgbsmaterialteamus@millercoors.com', 'MMD', 'VW_INFOSHEET_PRODUCTION', 'INFOSHEET_PRODUCTION', r'\\mbsus238\trfshare\Master Data\Data Cleansing\Audit Reports\Daily Reports\INFOSHEET_PRODUCTION.csv'], 
['INFOSHEET_FINANCE', (len(results35)), current_date, 'US', 'dlgbsmaterialteamus@millercoors.com', 'MMD', 'VW_INFOSHEET_FINANCE', 'INFOSHEET_FINANCE', r'\\mbsus238\trfshare\Master Data\Data Cleansing\Audit Reports\Daily Reports\INFOSHEET_FINANCE.csv'], 
['Material Not Costed or Not Approved', (len(results36)), current_date, 'US', 'DMCosting@molsoncoors.com, productcosting@molsoncoors.com', 'MMD', 'VW_PMSP_700_NOT_COST_NOT_APP', 'Material Not Costed or Not Approved', r'\\mbsus238\trfshare\Master Data\Data Cleansing\Audit Reports\Daily Reports\Material Not Costed or Not Approved.csv'], 
['040_MC_BRAND_ABRV_duplicate', (len(results37)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_MC_BRAND_ABRV_DUPLICATE', 'MD_MM_US_DL_040_MC_BRAND_ABRV_duplicate', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\040_MC_BRAND_ABRV_duplicate\040_MC_BRAND_ABRV_duplicate.csv'], 
['MSKU-BaseSKU PROMO', (len(results38)), current_date, 'US', 'DMOProductAuthorizat@molsoncoors.com ', 'PA', 'VW_BASEMSKU_PROMO', 'MSKU-BaseSKU PROMO', r'\\mbsus238\trfshare\DMO Master Data Reports\ReportsPA\MSKU-BaseSKU PROMO.csv'], 
['045_MSKU in MC Plant - OSKU Not in Plant', (len(results39)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_PLNT_710', 'MD_MM_US_DL_045_MSKU_in_MC_Plant_OSKU_Not_in_Plant', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\045_MSKU in MC Plant - OSKU Not in Plant\045_MSKU in MC Plant - OSKU Not in Plant.csv'], 
['BANK_DETAILS_RP9_400', (len(results40)), current_date, 'ONA', 'globalvendormaster@molsoncoors.com', 'VMD', 'NO', 'NO', r'\\mcebucfnpp01\SharedData\GBS\MD\Vendor Reports\BANK_DETAILS_RP9_400.csv'], 
['Tax Number 5 Format', (len(results42)), current_date, 'CA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_TAX_NUMBER_5_FORMAT_RP9_CA', 'Tax Number 5 Format', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\Tax_Number_5_Format'], 
['Tax Number 5', (len(results43)), current_date, 'CA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_TAX_NUMBER_5_RP9_CA', 'Tax Number 5', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\Tax_Number_5'], 
['Tax Number 5 Export', (len(results44)), current_date, 'CA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_TAX_NUMBER_5_EXPORT_RP9_CA', 'Tax Number 5 Export', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\Tax Number 5_Export'], 
['Capital letters_CA', (len(results45)), current_date, 'CA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_CAPITAL_LETTERS_RP9_CA', 'Capital letters_CA', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\Capital letters'], 
['LifeCycle_Status_CA', (len(results46)), current_date, 'CA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_LIFECYCLE_STATUS_RP9_CA', 'LifeCycle_Status_CA', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\LifeCycle_Status'], 
['Hierarchy_Assignment', (len(results47)), current_date, 'CA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_HIERARCHY_ASSIGNMENT', 'Hierarchy_Assignment', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\Hierarchy_Assignment'], 
['Hierarchy_7', (len(results48)), current_date, 'CA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_HIERARCHY_7', 'Hierarchy_7', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\Hierarchy_7'], 
['Tax_Applicable', (len(results49)), current_date, 'CA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_TAX_APPLICABLE', 'Tax_Applicable', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\Tax_Applicable'], 
['ONA Extension Check', (len(results50)), current_date, 'US', 'NO', 'MMD', 'NO', 'NO', 'NO'], 
['050_ZMSK MAT PROCURE F WITH NO SPECIAL PROCUREMENT COSTING', (len(results52)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'DM_MAT_AU_ZMSKPURCHASED_A10_SM', 'MD_MM_US_DL_050_ZMSK_MAT_PROCURE_F_WITH_NO_SPECIAL_PROCUREMENT_COSTING', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\050_ZMSK MAT PROCURE F WITH NO SPECIAL PROCUREMENT COSTING\050_ZMSK MAT PROCURE F WITH NO SPECIAL PROCUREMENT COSTING.csv'], 
['B_008_Backflush_Indicator_Audit_CA', (len(results53)), current_date, 'CA', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_REPORT_BACKFLUSH_INDICAT_CA', 'MD_MM_CA_DL_B_008_Backflush_Indicator_Audit_CA', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_008_Backflush_Indicator_Audit_CA'], 
['INFOSHEET_FINANCE_CA', (len(results54)), current_date, 'CA', 'scmdt@molsoncoors.com', 'MMD', 'VW_INFOSHEET_FINANCE_CA', 'INFOSHEET_FINANCE_CA', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\Aditional reports'], 
['INFOSHEET_PRODUCTION_CA', (len(results55)), current_date, 'CA', 'scmdt@molsoncoors.com', 'MMD', 'VW_INFOSHEET_PRODUCTION_CA', 'INFOSHEET_PRODUCTION_CA', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\Aditional reports'], 
['B_017_Material_Price_Unit_Not_Equal_To_1000', (len(results56)), current_date, 'CA', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_MCS_705_MC_MBEW_CA', 'MD_MM_CA_DL_B_017_Material_Price_Unit_Not_Equal_To_1000', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_017_Material_Price_Unit_Not_Equal_To_1000'], 
['B_037_ZRAW_Wrong_Batch_Management', (len(results57)), current_date, 'CA', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_WRONG_BATCH_MNGMT_ZRAW_CA', 'MD_MM_CA_DL_B_037_ZRAW_Wrong_Batch_Management', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_037_ZRAW_Wrong_Batch_Management'], 
['054_Hierarchy_Audit_check', (len(results58)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_HIERARCHY_US', 'MD_MM_US_DL_054_Hierarchy_Audit_check', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\054_Hierarchy_Audit_check\054_Hierarchy_Audit_check.csv'], 
['B_007_COSTED_AND_NOT_ACTIVATED', (len(results59)), current_date, 'CA', 'scmdt@molsoncoors.com', 'MMD', 'VW_COSTED_CA', 'B_007_COSTED_AND_NOT_ACTIVATED', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_007_COSTED_AND_NOT_ACTIVATED'], 
['3601_3610_WM_MISSING', (len(results60)), current_date, 'UK', 'MaterialMasterData.UK@molsoncoors.com', 'MMD', 'VW_WM_MISSING_3601_3610_RP9', '3601_3610_WM_MISSING', r'\\mcebucfnpp01\SharedData\GBS\MD\UK_SC_SQL_REPORTS\3601_3610_WM_MISSING\3601_3610_WM_MISSING.csv'], 
['WM_Allow_Additional_Stock', (len(results61)), current_date, 'UK', 'MaterialMasterData.UK@molsoncoors.com', 'MMD', 'VW_WM_ALLOW_ADD_STOCK_RP9', 'WM_Allow_Additional_Stock', r'\\mcebucfnpp01\SharedData\GBS\MD\UK_SC_SQL_REPORTS\WM_Allow_Additional_Stock\WM_Allow_Additional_Stock.csv'], 
['WM1_STOCK_3601', (len(results62)), current_date, 'UK', 'MaterialMasterData.UK@molsoncoors.com', 'MMD', 'VW_WM1_STOCK_3601_RP9', 'WM1_STOCK_3601', r'\\mcebucfnpp01\SharedData\GBS\MD\UK_SC_SQL_REPORTS\WM1_STOCK_3601\WM1_STOCK_3601.csv'], 
['059_Material Status 30 Price 1 Cent', (len(results64)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_PMSP_705_STATUS30PRICE1C', 'MD_MM_US_DL_059_Material_Status_30_Price_1_Cent', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\059_Material Status 30 Price 1 Cent\059_Material Status 30 Price 1 Cent.csv'], 
['060_Mismatch BOM vs PV', (len(results65)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_DM_AU_BOMPV_GF', 'MD_MM_US_DL_060_Mismatch_BOM_vs_PV', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\060_Mismatch BOM vs PV\060_Mismatch BOM vs PV.csv'], 
['065_BOM Missing Item', (len(results66)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_MISSING_BOM_ITEM_US', 'MD_MM_US_DL_065_BOM_Missing_Item', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\065_BOM Missing Item\065_BOM Missing Item.csv'], 
['Quebec Pricing Group', (len(results67)), current_date, 'CA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_QC_CONTACT_DETAILS', 'Quebec Pricing Group', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\Quebec Pricing Group'], 
['066_ZPCK_Batch_Management_Check', (len(results68)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_ZPCK_BATCH_MNGT_CHECK', 'MD_MM_US_DL_066_ZPCK_Batch_Management_Check', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\066_ZPCK_Batch_Management_Check\066_ZPCK_Batch_Management_Check.csv'], 
['Address details', (len(results69)), current_date, 'ONA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_ADDRESS_DETAILS', 'Address details', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\Address details\Address details.csv'], 
['Default flag for BP and PY', (len(results70)), current_date, 'ONA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_DEFAULT_FLAG', 'Default flag for BP and PY', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\Default flag for BP and PY\Default flag for BP and PY.csv'], 
['Payment term', (len(results71)), current_date, 'ONA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_PAYMENT_TERM', 'Payment term', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\Payment term\Payment term.csv'], 
['Phone number details', (len(results72)), current_date, 'ONA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_PHONE_NUMBER_DETAILS', 'Phone number details', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\Phone number details\Phone number details.csv'], 
['Price determination on Hierarchy nodes', (len(results73)), current_date, 'ONA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_PRICE_DETERMINATION', 'Price determination on Hierarchy nodes', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\Price determination on Hierarchy nodes\Price determination on Hierarchy nodes.csv'], 
['Special Characters', (len(results74)), current_date, 'ONA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_SPECIAL_CHARACTERS', 'Special Characters', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\Special Characters\Special Characters.csv'], 
['B_018_Material_Global_Sales_Org_Status_Comparison', (len(results75)), current_date, 'CA', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_LCS_739MatGlob_CA', 'MD_MM_CA_DL_B_018_Material_Global_Sales_Org_Status_Comparison', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_018_Material_Global_Sales_Org_Status_Comparison'], 
['B_019_Material_Global_Plant_Status_Comparison', (len(results76)), current_date, 'CA', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_LCS_736MatGlob_CA', 'MD_MM_CA_DL_B_019_Material_Global_Plant_Status_Comparison', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_019_Material_Global_Plant_Status_Comparison'], 
['Blocking Data', (len(results77)), current_date, 'ONA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_BLOCKING_DATA', 'Blocking Data', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\Blocking Data\Blocking Data.csv'], 
['Additional Data - Sales Area', (len(results78)), current_date, 'ONA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_ADD_DATA_SALES_AREA', 'Additional Data - Sales Area', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\Additional Data - Sales Area\Additional Data - Sales Area.csv'], 
['Ship-to assigned to 2 sold-to', (len(results79)), current_date, 'ONA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_SHIPTO_ASSGND_SOLDTO', 'Ship-to assigned to 2 sold-to', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\Ship-to assigned to 2 sold-to\Ship-to assigned to 2 sold-to.csv'], 
['ZV Function for Shipping Conditions', (len(results80)), current_date, 'ONA', 'g.cumada@molsoncoors.com', 'CMD', 'VW_ZF_FUNCTION_SHIPPING', 'ZV Function for Shipping Conditions', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\ZV Function for Shipping Conditions\ZV Function for Shipping Conditions.csv'], 
['B_091_SD_Not_A_Partner', (len(results81)), current_date, 'UK', 'GlobalCustomerMaster@molsoncoors.com', 'CMD', 'VW_203_UK', 'B_091_SD_Not_A_Partner', r'\\mcebucfnpp01\SharedData\GBS\MD\UK_SQL_REPORTS\B_091_SD_Not_A_Partner'], 
['B_092_AM_Alignment', (len(results82)), current_date, 'UK', 'GlobalCustomerMaster@molsoncoors.com', 'CMD', 'VW_204_UK', 'B_092_AM_Alignment', r'\\mcebucfnpp01\SharedData\GBS\MD\UK_SQL_REPORTS\B_092_AM_Alignment'], 
['B_093_RD_Alignment', (len(results83)), current_date, 'UK', 'GlobalCustomerMaster@molsoncoors.com', 'CMD', 'VW_205_UK', 'B_093_RD_Alignment', r'\\mcebucfnpp01\SharedData\GBS\MD\UK_SQL_REPORTS\B_093_RD_Alignment'], 
['B_094_BDM_Alignment', (len(results84)), current_date, 'UK', 'GlobalCustomerMaster@molsoncoors.com', 'CMD', 'VW_206_UK', 'B_094_BDM_Alignment', r'\\mcebucfnpp01\SharedData\GBS\MD\UK_SQL_REPORTS\B_094_BDM_Alignment'], 
['B_095_RD_Sales_District_Alignment', (len(results85)), current_date, 'UK', 'GlobalCustomerMaster@molsoncoors.com', 'CMD', 'VW_207_UK', 'B_095_RD_Sales_District_Alignment', r'\\mcebucfnpp01\SharedData\GBS\MD\UK_SQL_REPORTS\B_095_RD_Sales_District_Alignment'], 
['071_MSKU_BOM_COMPONENT_CHECK', (len(results86)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_MSKU_COMP_AUDIT', 'MD_MM_US_DL_071_MSKU_BOM_COMPONENT_CHECK', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\071_MSKU_BOM_COMPONENT_CHECK\071_MSKU_BOM_COMPONENT_CHECK.csv'], 
['RO_REGION_BEER', (len(results87)), current_date, 'ROBG', 'GlobalCustomerMaster@molsoncoors.com', 'CMD', 'VW_RO_REGION_BEER', '\ROBG_009_RO_REGION_BEER', r'\\mcebucfnpp01\SharedData\GBS\MD\ROBG_SQL_REPORTS\ROBG_009_RO_REGION_BEER\RO_REGION_BEER.csv '], 
['FX_RATES_CHECK', (len(results88)), current_date, 'ROBG', 'sapdatabasesupportrobg@molsoncoors.com', 'CMD', 'VW_RO_BG_FX_RATES_CHECK', 'FX_RATES_CHECK', r'\\mcebucfnpp01\SharedData\GBS\MD\ROBG_SQL_REPORTS\ROBG_010_RO_BG_ FX_Rates'], 
['B_05_UK_Costing_report', (len(results89)), current_date, 'UK', 'MaterialMasterData.UK@molsoncoors.com', 'MMD', 'VW_214_UK', 'B_05_UK_Costing_report', r'\\mcebucfnpp01\SharedData\GBS\MD\UK_SC_SQL_REPORTS\B_05_UK_Costing_report'], 
['B_072_ZWIP_ZMSK_MATERIALS_PROCUREMENT_E_WITH_NO_BOM', (len(results90)), current_date, 'CA', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_245_CA', 'MD_MM_CA_DL_B_072_ZWIP_ZMSK_MATERIALS_PROCUREMENT_E_WITH_NO_BOM', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_072_ZWIP_ZMSK_MATERIALS_PROCUREMENT_E_WITH_NO_BOM'], 
['B_092_MSKU_BOM_COMPONENT_CHECK', (len(results91)), current_date, 'CA', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_246_CA', 'MD_MM_CA_DL_B_092_MSKU_BOM_COMPONENT_CHECK', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_092_MSKU_BOM_COMPONENT_CHECK'], 
['B_070_Wrong_Costing_Relevancy_on_BOM_Components', (len(results92)), current_date, 'CA', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_244_CA', 'MD_MM_CA_DL_B_070_Wrong_Costing_Relevancy_on_BOM_Components', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_070_Wrong_Costing_Relevancy_on_BOM_Components'], 
['B_075_BOM_VOLUME_CHECK_ZWIP', (len(results93)), current_date, 'CA', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_247_CA', 'MD_MM_CA_DL_B_075_BOM_VOLUME_CHECK_ZWIP', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_075_BOM_VOLUME_CHECK_ZWIP'], 
['Region_CA_Customers', (len(results94)), current_date, 'CA', 'g.cumada@molsoncoors.com', 'MMD', 'VW_REGION_CANADA_CUSTOMERS', 'Region_CA_Customers', r'\\mcebucfnpp01\SharedData\GBS\MD\CA_CUST_RP9_SQL_REPORTS\Region_CA_Customers'], 
['B_093_BOM_VOLUME_CHECK_ZPCK', (len(results95)), current_date, 'CA', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_254_CA', 'MD_MM_CA_DL_B_093_BOM_VOLUME_CHECK_ZPCK', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_093_BOM_VOLUME_CHECK_ZPCK'], 
['B_082_ZWIP_BOM_Recursiveness_Indicator', (len(results96)), current_date, 'CA', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_255_CA', 'MD_MM_CA_DL_B_082_ZWIP_BOM_Recursiveness_Indicator', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_082_ZWIP_BOM_Recursiveness_Indicator'], 
['B_106_MSKU_OSKU_Distribution_Channel_40_50_check', (len(results97)), current_date, 'CA', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_256_CA', 'MD_MM_CA_DL_B_106_MSKU_OSKU_Distribution_Channel_40_50_check', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_106_MSKU_OSKU_Distribution_Channel_40_50_check'], 
['B_091_ZPCK_Batch_Management_Check', (len(results98)), current_date, 'CA', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_257_CA', 'MD_MM_CA_DL_B_091_ZPCK_Batch_Management_Check', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_091_ZPCK_Batch_Management_Check'], 
['076_MD_MM_NA_Price_per_unit', (len(results99)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_PRICE_PER_UNIT', 'MD_MM_US_DL_076_MD_MM_NA_Price_per_unit', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\076_MD_MM_NA_Price_per_unit\076_MD_MM_NA_Price_per_unit.csv'], 
['A_139_Batch_Flag_ZFER', (len(results100)), current_date, 'UK', 'MaterialMasterData.UK@molsoncoors.com', 'MMD', 'VW_210_UK', '\A_139_Batch_Flag_ZFER', r'\\mcebucfnpp01\SharedData\GBS\MD\UK_SC_SQL_REPORTS\A_139_Batch_Flag_ZFER'], 
['B_088_MSKU_VOLUME_CHECK', (len(results101)), current_date, 'CA', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_MSKU_VOL_CHECK_CA', 'MD_MM_CA_DL_B_088_MSKU_VOLUME_CHECK', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_088_MSKU_VOLUME_CHECK'], 
['B_111_MISSING_EXCISE_DUTY', (len(results102)), current_date, 'CA', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_259_CA', 'MD_MM_CA_DL_B_111_MISSING_EXCISE_DUTY', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_111_MISSING_EXCISE_DUTY'], 
['B_055_Duplicate_Description_check', (len(results103)), current_date, 'CA', 'scmdt@molsoncoors.com', 'MMD', 'VW_234_CA', 'MD_MM_CA_DL_B_055_Duplicate_Description_check', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_055_Duplicate_Description_check'], 
['B_069_Material_Beverage_Misalignment', (len(results104)), current_date, 'CA', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_260_CA', 'MD_MM_CA_DL_B_069_Material_Beverage_Misalignment', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_069_Material_Beverage_Misalignment'], 
['A_097_BOG_COG_Sales_District', (len(results105)), current_date, 'UK', 'GlobalCustomerMaster@molsoncoors.com, Steve.Symonds@molsoncoors.com', 'CMD', 'VW_217_UK', 'A_097_BOG_COG_Sales_District', r'\\mcebucfnpp01\SharedData\GBS\MD\UK_SQL_REPORTS\A_097_BOG_COG_Sales_District'], 
['B_114_Material_in_status_10_with_PV', (len(results106)), current_date, 'CA', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_263_CA', 'MD_MM_CA_DL_B_114_Material_in_status_10_with_PV', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_114_Material_in_status_10_with_PV'], 
['079_Material_in_status_10_with_PV', (len(results107)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD', 'VW_PV_MAT_ST_10', 'MD_MM_US_DL_079_Material_in_status_10_with_PV', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\079_Material_in_status_10_with_PV\079_Material_in_status_10_with_PV.csv'],
['080_WH_Storage_Condition', (len(results108)), current_date, 'US', 'NO', 'MMD', 'NO'],
['081_MSKU_MRP2_StorLoc_checks', (len(results109)), current_date, 'US', 'NO', 'MMD', 'NO'],
['ACTIVATION REQUEST REPORT', (len(results110)), current_date, 'UK', 'MaterialMasterData.UK@molsoncoors.com', 'MMD' , 'VW_220_UK', 'ACTIVATION REQUEST REPORT', r'\\mcebucfnpp01\SharedData\GBS\MD\UK_SC_SQL_REPORTS\ACTIVATION REQUEST REPORT'],
['086_ZPCK_MSKU_status30_noprice', (len(results111)), current_date, 'US', 'gbs_masterdatareports@molsoncoors.com', 'MMD' , 'VW_ZPCK_MSKU_STS30_NOPRICE', 'MD_MM_US_DL_086_ZPCK_MSKU_status30_noprice', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\086_ZPCK_MSKU_status30_noprice'],
['B_086_Hierarchy_Audit_check', (len(results112)), current_date, 'CA', 'gbs_masterdatareports@molsoncoors.com', 'MMD' , 'VW_272_CA', 'MD_MM_CA_DL_B_086_Hierarchy_Audit_check', r'\\mcebucfnpp01\SharedData\GBS\MD\SQL_RP9_CA_MAT\B_086_Hierarchy_Audit_check']
]



#with open("//mcebucfnpp01/SharedData/GBS/MD/SQL Scripts and Batch files/Python Scripts/COUNT_DAILY_AISE.csv", 'a', encoding='utf-8', newline='') as f:

with open("//mcebucfnpp01/SharedData/GBS/MD/SQL_EXPORT/Count_Reports.csv", 'a', encoding='utf-8', newline='') as f:


    writer = csv.writer(f)

    # write the header
    #if f.tell() == 0:
    #writer.writerow(header)
    

    #write multiple rows
    writer.writerows(data)





