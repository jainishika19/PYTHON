import time
import os

# Define purple color and reset
purple = "\033[95m"
reset = "\033[0m"

# Two heart sizes (small and big)
heart1 = [
"           ***           ***",
"        *******       *******",
"      ***********   ***********",
"     ***************************",
"     ***************************",
"      *************************",
"        *********************",
"          *****************",
"            *************",
"              *********",
"                *****",
"                  *"
]

heart2 = [
"            ***             ***",
"        **********       **********",
"      **************   **************",
"     *******************************",
"     ********************************",
"      ******************************",
"        **************************",
"          **********************",
"            ******************",
"              **************",
"                **********",
"                  ******",
"                    **"
]

# Animation loop
while True:
    os.system("cls" if os.name == "nt" else "clear")  # clear screen
    for line in heart1:
        print(purple + line + reset)
    print(purple + "        LOVE YOURSELF 💜" + reset)
    time.sleep(0.5)

    os.system("cls" if os.name == "nt" else "clear")
    for line in heart2:
        print(purple + line + reset)
    print(purple + "        LOVE YOURSELF 💜" + reset)
    time.sleep(0.5)