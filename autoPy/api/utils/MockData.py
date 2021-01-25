
class MockData(object):
    def get_mock_param(self,mocker,mock_path,mock_result,side_effect):
        mock_api =mocker.patch(mock_path,return_value=mock_result,side_effect=side_effect)
        #mock_api = mocker.patch.object("class_name","method_name","mock_result","side_effect")
        return mock_api

if __name__ == '__main__':
    print("11")