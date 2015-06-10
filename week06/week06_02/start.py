from directed_graph import DirectedGraph
import requests


class WhoFollowsWho:

    def __init__(self, username, level = 0):
        self.resource = "https://api.github.com/users/{}".format(username)
        self.__username = username
        self.__level = level
        self.__graph = DirectedGraph()

    def do_you_follow(self, user):
        return user in self.__get_followings(self.__username)

    def __get_followings(self, user):
        user_resource = "https://api.github.com/users/{}".format(user)
        r = requests.get(user_resource + "/following").json()
        followings = [x["login"] for x in r]

        return followings


    def does_he_she_follows(self, user):
        return  user in self.__get_followers(self.__username)

    def __get_followers(self, user):
        user_resource = "https://api.github.com/users/{}".format(user)
        r = requests.get(user_resource + "/followers").json()
        followers = [x["login"] for x in r]

        return followers

    def construct_graph(self, user, level):
        pass


 
def main():
    wh = WhoFollowsWho("bgvladedivac", 2)
    #print(wh.do_you_follow("RadoRado"))  
    #print(wh.does_he_she_follows("miglen")) # == True


if __name__ == '__main__':
    main()