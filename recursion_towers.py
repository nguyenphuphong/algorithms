# Denote:
# Source Tower: S
# Destination Tower: D
# Intermedia Tower: I
#
# We can see the recursion is that, to solve the puzzle of n disks
# We need to move n-1 disk from S to I
# The move the largest disk from S to D
# After that we move n-1 disk from I to D
def tower(n, source, intermediate, destination):
    if n == 1:
        print('Move Disk {} from {} to {}'.format(n, source, destination))
    else:
        tower(n - 1, source, destination, intermediate)

        print('Move Disk {} from {} to {}'.format(n, source, destination))

        tower(n - 1, intermediate, source, destination)

tower(3, 'A', 'B', 'C')

# T(1) = 1
# T(2) = 3
# T(n) = 2T(n - 1) + 1
#
# O(n) = 2^n
