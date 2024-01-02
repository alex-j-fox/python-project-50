from typing import Dict, Any


def get_diff(data1: Dict[str, Any], data2: Dict[str, Any]) -> Dict[str, Any]:
    """Возвращает сортированный обьединенный словарь двух исходных словарей,
    где ключ 'key' содержит значение с именем ключа-родителя,
    'status' содержит текущее состояние родителя ('удален', 'добавлен',
    'обновлен', 'без изменений', 'вложенный'),
    'value' содержит значение родителя из исходного словаря,
    'value_upd' содержит обновленное значение родителя

    :param data1: Первый сравниваемый словарь
    :type data1: Dict[str, Any]
    :param data2: Второй сравниваемый словарь
    :type data2: Dict[str, Any]
    :return: Обьединенный сортированный словарь
    :rtype: Dict[str, Any]
    """
    total_dict = {}
    sorted_keys = sorted({**data1, **data2})
    for key in sorted_keys:
        if key not in data2:
            total_dict[key] = {
                'key': key,
                'status': 'removed',
                'value': data1[key]
            }
        elif key not in data1:
            total_dict[key] = {
                'key': key,
                'status': 'added',
                'value': data2[key]
            }
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            total_dict[key] = {
                'key': key,
                'status': 'nested',
                'value': get_diff(data1[key], data2[key])
            }
        elif data1[key] != data2[key]:
            total_dict[key] = {
                'key': key,
                'status': 'updated',
                'value': data1[key],
                'value_upd': data2[key]
            }
        else:
            total_dict[key] = {
                'key': key,
                'status': 'unchanged',
                'value': data1[key]
            }
    return total_dict
