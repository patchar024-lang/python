def manual_shutdown():
    print("\n[Shutdown] User canceled the program. Exiting cleanly...")

try:
    print("Press Ctrl+C to stop the loop...")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    manual_shutdown()