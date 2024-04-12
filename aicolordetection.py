import cv2
import numpy as np
import pyautogui

# Definiuj zakres koloru "rgba(255,40,40,255)" w formacie BGR
target_color = (40, 40, 255)

# Utwórz okno do wyświetlania obrazu z wykrytym kolorem
cv2.namedWindow("Custom Color Detection", cv2.WINDOW_NORMAL)

while True:
    # Przechwyć obraz z ekranu
    screenshot = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Utwórz maskę dla określonego koloru
    lower_color = np.array([target_color[0] - 10, target_color[1] - 10, target_color[2] - 10])
    upper_color = np.array([target_color[0] + 10, target_color[1] + 10, target_color[2] + 10])
    mask = cv2.inRange(frame, lower_color, upper_color)

    # Znajdź kontury obiektów o określonym kolorze
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Oznacz obszary wykrytego koloru na ekranie
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:  # minimalny rozmiar obszaru
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, "Target Color", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Wyświetl obraz w oknie
    cv2.imshow("Custom Color Detection", frame)

    # Przerwij pętlę, jeśli naciśnięto klawisz 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Zamknij wszystkie okna po zakończeniu
cv2.destroyAllWindows()
