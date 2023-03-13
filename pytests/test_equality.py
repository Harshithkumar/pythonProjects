def test_equality():
   # with pytest.raises(AssertionError) as e:
       assert 100 == 200

def test_greater_equal():
   num = 100
   print("This test is to check which is greater and it is passed !")
   assert num >= 100

def test_less():
   num = 100
   assert num < 200
   print("\n Testing is it is printing after assert statement")
   test_greater_equal()

def test_module_3(local_testing):
    assert 9 * local_testing == 81
