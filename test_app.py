from app import main

def test_main(capfd):
    main()
    captured = capfd.readouterr().out.strip()
    assert captured == "Github CICD test!"
