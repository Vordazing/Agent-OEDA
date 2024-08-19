import React, { useState, useCallback } from 'react';
import { Table, Button, Input, Popconfirm, Form, Modal, Select, message } from 'antd';
import { EditOutlined, DeleteOutlined, PlusOutlined } from '@ant-design/icons';
import axios from 'axios'; // Если вы используете axios для отправки запросов

const { Option } = Select;

const Tables = () => {
  const [dataSource, setDataSource] = useState([]);
  const [editingKey, setEditingKey] = useState('');
  const [isModalVisible, setIsModalVisible] = useState(false);
  const [form] = Form.useForm();
  const [currentRecord, setCurrentRecord] = useState(null);
  const [monitoring, setMonitoring] = useState('1'); // По умолчанию выбрано "Мониторинг 1"

  // Handles adding new record
  const handleAdd = () => {
    setIsModalVisible(true);
    setCurrentRecord(null); // Indicate new record
    form.resetFields();
  };

  // Handles editing existing record
  const handleEdit = (record) => {
    setIsModalVisible(true);
    setCurrentRecord(record);
    form.setFieldsValue(record);
    setEditingKey(record.key);
  };

  // Handles deleting a record
  const handleDelete = (key) => {
    setDataSource(dataSource.filter(item => item.key !== key));
  };

  // Saves or updates the record
  const handleSave = () => {
    form.validateFields()
      .then(values => {
        if (currentRecord) {
          // Edit existing record
          setDataSource(dataSource.map(item => item.key === currentRecord.key ? { ...item, ...values } : item));
        } else {
          // Add new record
          const newKey = `${dataSource.length + 1}`;
          setDataSource([...dataSource, { key: newKey, ...values }]);
        }
        setIsModalVisible(false);
      });
  };

  // Handles cancelling the form
  const handleCancel = () => {
    setIsModalVisible(false);
  };

  // Handles paste event
  const handlePaste = useCallback((event) => {
    event.preventDefault();
    const clipboardData = event.clipboardData || window.clipboardData;
    const pastedData = clipboardData.getData('Text');
    const rows = pastedData.split('\n').map(row => row.split('\t'));
    const newRows = rows.map((row, index) => ({
      key: (dataSource.length + index + 1).toString(),
      hostname: row[0] || '',
      ip: row[1] || '',
      worker: row[2] || '',
      MAC: row[3] || '',
      sn: row[4] || '',
      owner: row[5] || '',
    }));
    setDataSource([...dataSource, ...newRows]);
  }, [dataSource]);

  // Handles select change
  const handleMonitoringChange = (value) => {
    setMonitoring(value);
  };


  const handleSubmit = () => {
    if (dataSource.length === 0) {
      message.warning('Таблица пуста. Нечего отправлять.');
      return;
    }
  
    const dataToSend = {
      monitoring,
      records: dataSource
    };
  
    console.log('Отправляемые данные:', dataToSend);
    
    axios.post('http://0.0.0.0:8000/submit', dataToSend)
      .then(response => {
        message.success('Данные успешно отправлены');
        setDataSource([]); // Очищаем таблицу после успешной отправки
      })
      .catch(error => {
        message.error('Ошибка при отправке данных');
      });
  };
  

  // Columns definition
  const columns = [
    {
      title: 'Hostname',
      dataIndex: 'hostname',
      key: 'hostname',
      editable: true,
    },
    {
      title: 'IP Address',
      dataIndex: 'ip',
      key: 'ip',
      editable: true,
    },
    {
      title: 'Worker',
      dataIndex: 'worker',
      key: 'worker',
      editable: true,
    },
    {
      title: 'MAC Address',
      dataIndex: 'MAC',
      key: 'MAC',
      editable: true,
    },
    {
      title: 'Serial Number',
      dataIndex: 'sn',
      key: 'sn',
      editable: true,
    },
    {
      title: 'Владелец',
      dataIndex: 'owner',
      key: 'owner',
      editable: true,
    },
    {
      title: 'Действие',
      key: 'action',
      render: (_, record) => (
        <span>
          <Button
            icon={<EditOutlined />}
            onClick={() => handleEdit(record)}
            style={{ marginRight: 8 }}
          />
          <Popconfirm
            title="Удалить?"
            onConfirm={() => handleDelete(record.key)}
            okText="Yes"
            cancelText="No"
          >
            <Button icon={<DeleteOutlined />} />
          </Popconfirm>
        </span>
      ),
    },
  ];

  return (
    <div style={{ padding: 20 }}>
      <h2>Добавление ASIC в Awesome</h2>
      <Button
        type="primary"
        icon={<PlusOutlined />}
        onClick={handleAdd}
        style={{ marginBottom: 16 }}
      >
        Добавить ASIC
      </Button>
      <div
        onPaste={handlePaste}
        style={{ border: '1px solid #ddd', padding: 20, minHeight: 100, marginBottom: 20 }}
      >
        <p>Вставьте сюда свои данные (из буфера обмена), чтобы добавить несколько записей.</p>
      </div>
      <Table
        dataSource={dataSource}
        columns={columns}
        rowKey="key"
      />
      <div style={{ marginTop: 20, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <Select defaultValue="1" style={{ width: 200 }} onChange={handleMonitoringChange}>
          <Option value="1">Мониторинг 1</Option>
          <Option value="2">Мониторинг 2</Option>
          <Option value="3">Мониторинг 3</Option>
        </Select>
        <Button
        type="primary"
        onClick={handleSubmit}
        style={{ marginLeft: 16 }}>
          Отправить данные
        </Button>
</div>

      <Modal
        title={currentRecord ? 'Изменить ASIC' : 'Добавить ASIC'}
        open={isModalVisible}
        onOk={handleSave}
        onCancel={handleCancel}
      >
        <Form
          form={form}
          layout="vertical"
          name="form_in_modal"
        >
          <Form.Item
            name="hostname"
            label="Hostname"
          >
            <Input />
          </Form.Item>
          <Form.Item
            name="ip"
            label="IP Address"
          >
            <Input />
          </Form.Item>
          <Form.Item
            name="worker"
            label="Worker"
          >
            <Input />
          </Form.Item>
          <Form.Item
            name="MAC"
            label="MAC Address"
          >
            <Input />
          </Form.Item>
          <Form.Item
            name="sn"
            label="Serial Number"
          >
            <Input />
          </Form.Item>
          <Form.Item
            name="owner"
            label="Владелец"
          >
            <Input />
          </Form.Item>
        </Form>
      </Modal>
    </div>
  );
};

export default Tables;
