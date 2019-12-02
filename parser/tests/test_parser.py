import sys, os, unittest
sys.path.append("..")
from main.executers import SequentialExecuter

class TestExampleSql(unittest.TestCase):
    def setUp(self) -> None:
        self.cte_parsed = ["['MYVIEW', 'cte.sql', 'SALES.ORDERS']",
            "['MYVIEW', 'cte.sql', 'A']",
            "['MYVIEW', 'cte.sql', 'SALES.ORDER_ITEMS']",
            "['MYVIEW', 'cte.sql', 'SALES.STAFFS']"]

    def tearDown(self) -> None:
        pass

    def test_cte(self):
        self.executor = SequentialExecuter()
        base = os.path.dirname(os.path.abspath(__file__))
        base_parent = os.path.dirname(base)
        sd = os.path.join(base_parent, 'exampleSql')
        file = os.path.join(sd, 'cte.sql')
        self.executor.to_parse_files = [file]
        result = self.executor.run()
        tab_deps_array=[]
        for sqlobject in result:
            for table in sqlobject['tables']:
                tab_deps = str([sqlobject['name'],
                                sqlobject['filename'],
                                table])
                tab_deps_array.append(tab_deps)
            self.assertEqual(tab_deps_array, self.cte_parsed)



if __name__ == '__main__':
    unittest.main()

# ['MYVIEW', 'cte.sql', 'SALES.ORDERS', '26135d68-1509-11ea-9d61-5c879ca86492']
# ['MYVIEW', 'cte.sql', 'A', '26135d69-1509-11ea-b48c-5c879ca86492']
# ['MYVIEW', 'cte.sql', 'SALES.ORDER_ITEMS', '26135d6a-1509-11ea-874a-5c879ca86492']
# ['MYVIEW', 'cte.sql', 'SALES.STAFFS', '26135d6b-1509-11ea-a7b1-5c879ca86492']
# [None, 'old-join.sql', 'CUSTOMERS', '26135d6c-1509-11ea-8868-5c879ca86492']
# [None, 'old-join.sql', 'ORDERS', '26135d6d-1509-11ea-aeee-5c879ca86492']
# [None, 'old-join.sql', 'PRODUCT', '26135d6e-1509-11ea-b8bd-5c879ca86492']
# ['SAMP.V1', 'old-view.sql', 'AE_CONFIG.EMPLOYEE', '26135d6f-1509-11ea-821b-5c879ca86492']
# [None, 'third.sql', 'P.PBD_PROD_NAME', '26135d70-1509-11ea-aad1-5c879ca86492']
# [None, 'third.sql', 'A.ACA_CU_NAME', '26135d71-1509-11ea-ad68-5c879ca86492']
# [None, 'third.sql', 'ADMIN.SFFACA_DETAILS', '26135d72-1509-11ea-8975-5c879ca86492']
# [None, 'third.sql', 'ACA_TXT_L1', '26135d73-1509-11ea-9954-5c879ca86492']
# [None, 'third.sql', 'ADMIN.SFFACA_OTHER', '26135d74-1509-11ea-a5bb-5c879ca86492']
# [None, 'third.sql', 'A.ACA_CU_NAME', '26135d75-1509-11ea-9dd5-5c879ca86492']
# [None, 'third.sql', 'ADMIN.SFFACA_DETAILS', '26135d76-1509-11ea-a52d-5c879ca86492']
# [None, 'third.sql', 'ACA_TXT_L1', '26135d77-1509-11ea-ac2d-5c879ca86492']
# [None, 'third.sql', 'ADMIN.SFFACA_OTHER', '26135d78-1509-11ea-a453-5c879ca86492']
# [None, 'third.sql', 'P.PBD_PROD_NAME', '26135d79-1509-11ea-955f-5c879ca86492']
# [None, 'third.sql', 'ADMIN.SFFBSJ', '26135d7a-1509-11ea-b981-5c879ca86492']
# [None, 'third.sql', 'ADMIN.SFFPBD', '26135d7b-1509-11ea-a9e1-5c879ca86492']
# [None, 'third.sql', 'ADMIN.SFFPSD', '26135d7c-1509-11ea-9082-5c879ca86492']
# [None, 'third.sql', 'ADMIN.SFFPXD_DETAILS', '26135d7d-1509-11ea-acf1-5c879ca86492']
