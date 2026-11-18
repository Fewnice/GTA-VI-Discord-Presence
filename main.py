import time
from pypresence import DiscordNotFound, Presence

clientid = "1445160676522856458"

# Discord usernames: fewnice and oll.a

def main():
    rpc = None

    try:
        rpc = Presence(clientid)
        rpc.connect()
        rpc.update(
            details="Exploring Vice City",
            state="Story Mode",
            start=int(time.time())
        )

        print("GTA VI Rich Presence is active.")
        print("Press Ctrl+C to stop.")

        while True:
            time.sleep(15)

    except DiscordNotFound:
        print("Discord Desktop was not found. Open Discord and try again.")
    except KeyboardInterrupt:
        print("\nRich Presence stopped.")
    except Exception as error:
        print(f"Error: {error}")
    finally:
        if rpc is not None:
            try:
                rpc.close()
            except Exception:
                pass


main()
