import kaixin, liangyu, tongfei, yangyang, gengxin, maggie
TEAM_NAME = "TEAM-AAAAAA"
def print_team():
  print(f"This is Team {TEAM_NAME}. We are:")
  print(kaixin.get_my_name())
  print(liangyu.get_my_name())
  print(tongfei.get_my_name())
  print(yangyang.my_name())
  print(gengxin.get_my_name())
  print(maggie.get_my_name())
if __name__ == "__main__":
  print_team()
