class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    return user in group.users or any(is_user_in_group(user, sub_group) for sub_group in group.get_groups())


if __name__ == "__main__":
    # test case 1
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print("Pass" if is_user_in_group(sub_child_user, parent) else "False")

    # test case 2
    group_1 = Group("Group1")
    group_2 = Group("Group2")
    group_1_sub1 = Group("Group1 Sub1")
    group_1_sub2 = Group("Group1 Sub2")
    group_1_sub3 = Group("Group1 Sub3")
    group_1_sub2_sub_child1 = Group("Group1 Sub2 SubChild1")

    target_user = "Seungyeon"
    group_1_sub2_sub_child1.add_user(target_user)

    group_1_sub2_users = [f"group_1_sub2_{i}" for i in range(10)]
    for user in group_1_sub2_users:
        group_1_sub2.add_user(user)

    group_1_users = [f"group_1_user_{i}" for i in range(4)]
    for user in group_1_users:
        group_1.add_user(user)

    group_1_sub2.add_group(group_1_sub2_sub_child1)
    group_1_groups = [group_2, group_1_sub1, group_1_sub2, group_1_sub3]
    for group in group_1_groups:
        group_1.add_group(group)

    print("Pass" if is_user_in_group(target_user, group_1) else "False")

    # test case 3
    print("Pass" if is_user_in_group("Udacity", group_1) == False else "False")
