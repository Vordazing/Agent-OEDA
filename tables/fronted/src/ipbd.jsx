import React, { useState, useEffect } from 'react';
import { Table, Button, message, Select } from 'antd';
import axios from 'axios';

const { Option } = Select;

const Ipbd = () => {
  const [tableData, setTableData] = useState([]);
  const [monitoringType, setMonitoringType] = useState(null);

  const columns = [
    {
      title: 'IP Address',
      dataIndex: 'ip_address',
      key: 'ip_address',
      align: 'center',
    },
    {
      title: 'Hostname',
      dataIndex: 'hostname',
      key: 'hostname',
      align: 'center',
    },
    {
      title: 'Serial Number',
      dataIndex: 'serial_number',
      key: 'serial_number',
      align: 'center',
    }
  ];

  const fetchData = async (monitoringType) => {
    try {
      const response = await axios.get(`http://0.0.0.0:8000/${monitoringType}`);
      const data = response.data.map((item, index) => ({
        key: index, // Уникальный ключ для каждой строки
        ip_address: item.ip_address,
        hostname: item.hostname,
        serial_number: item.serial_number,
      }));

      setTableData(data);
    } catch (error) {
      console.error('Ошибка загрузки данных:', error);
    }
  };

  useEffect(() => {
    if (monitoringType) {
      fetchData(monitoringType);

      // Устанавливаем интервал опрашивания каждые 10 секунд
      const intervalId = setInterval(() => {
        fetchData(monitoringType);
      }, 10000);

      // Очищаем интервал при размонтировании компонента
      return () => clearInterval(intervalId);
    }
  }, [monitoringType]);

  const handleSelectChange = (value) => {
    setMonitoringType(value);
  };

  const clearTable = async () => {
    if (!monitoringType) {
      message.error('Пожалуйста, выберите тип мониторинга перед очисткой.');
      return;
    }

    try {
      await axios.post(`http://0.0.0.0:8000/${monitoringType}/clear`);
      setTableData([]); // Очистка данных таблицы на клиенте
      message.success('Таблица очищена успешно!');
    } catch (error) {
      console.error('Ошибка при очистке таблицы:', error);
      message.error('Не удалось очистить таблицу.');
    }
  };

  const copyToClipboard = () => {
    const dataToCopy = tableData.map(row => `${row.ip_address}\t${row.hostname}\t${row.serial_number}`).join('\n');
    navigator.clipboard.writeText(dataToCopy)
      .then(() => {
        message.success('Данные скопированы в буфер обмена!');
      })
      .catch(() => {
        message.error('Не удалось скопировать данные.');
      });
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', margin: '20px', width: '80%' }}>
      <h2 style={{ textAlign: 'center', marginBottom: '20px' }}>IP в БД</h2>
      
      <Select
        placeholder="Выберите мониторинг"
        style={{ width: 200, marginBottom: '20px' }}
        onChange={handleSelectChange}
      >
        <Option value="mon1">Мониторинг 1</Option>
        <Option value="mon2">Мониторинг 2</Option>
        <Option value="mon3">Мониторинг 3</Option>
      </Select>

      <Table
        columns={columns}
        dataSource={tableData}
        pagination={false}
        style={{ width: '100%' }}
      />

      <div style={{ width: '100%', display: 'flex', justifyContent: 'flex-end', marginTop: '10px', gap: '10px' }}>
        <Button type="primary" onClick={clearTable}>
          Очистить таблицу
        </Button>
        <Button type="default" onClick={copyToClipboard}>
          Копировать
        </Button>
      </div>
    </div>
  );
};

export default Ipbd;
