import cv2
import numpy as np
import pyautogui

# Rozpoczęcie przechwytywania ekranu
cv2.namedWindow("Real-time Motion Detection", cv2.WINDOW_NORMAL)

# Pobierz pierwszą klatkę jako tło
screenshot = pyautogui.screenshot()
background = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

while True:
    # Przechwyć obraz z ekranu
    screenshot = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    # Oblicz różnicę między aktualną klatką a tłem
    diff = cv2.absdiff(frame, background)

    # Zastosuj progowanie, aby uzyskać obszary z znaczącymi zmianami
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # Znajdź kontury obszarów z ruchem
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Oznacz obszary z ruchem na ekranie
    for contour in contours:
        if cv2.contourArea(contour) > 500: # minimalny rozmiar obszaru
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Motion", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Wyświetl obraz w oknie
    cv2.imshow("Real-time Motion Detection", frame)

    # Aktualizacja tła (kolejna klatka)
    background = frame

    # Przerwij pętlę, jeśli naciśnięto klawisz 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Zamknij wszystkie okna po zakończeniu
cv2.destroyAllWindows()
