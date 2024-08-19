import React from 'react';
import { Row, Col, Card } from 'antd';
import { Link } from 'react-router-dom';

const menuItems = [
  { title: 'IP в БД', url: '/ipbd' },
  { title: 'Добавление ASIC в Awesome', url: '/addasic' },
  { title: 'В разработке ... 🛠', url: '#' },
  { title: '🔐', url: '#' },
  { title: '🔐', url: '#' },
  { title: '🔐', url: '#' },
];

const MenuGrid = () => {
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh' }}>
      <Row gutter={[16, 16]} justify="center" style={{ width: '100%', maxWidth: 1200 }}>
        {menuItems.map((item, index) => (
          <Col key={index} xs={24} sm={12} md={8}>
            <Link to={item.url} style={{ textDecoration: 'none' }}>
              <Card hoverable style={{ textAlign: 'center' }}>
                <h3>{item.title}</h3>
              </Card>
            </Link>
          </Col>
        ))}
      </Row>
    </div>
  );
};

export default MenuGrid;
