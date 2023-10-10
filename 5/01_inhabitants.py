# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import room_1 as room_1
import room_2 as room_2

room1_habitats = ", ".join(room_1.folks) + "."

room2_habitats = ", ".join(room_2.folks) + "."

print("В комнате room_1 живут:", room1_habitats)
print("В комнате room_2 живут:", room2_habitats)


