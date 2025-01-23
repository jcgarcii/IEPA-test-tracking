from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the MySQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://user:password@mysql_container/test_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Sources Table
class Source(db.Model):
    Source_ID = db.Column(db.Integer, primary_key=True)
    Source_Name = db.Column(db.String(255), nullable=False)
    Region = db.Column(db.String(255))
    Address = db.Column(db.String(255))
    City = db.Column(db.String(255))
    County = db.Column(db.String(255))
    Street = db.Column(db.String(255))
    Zip_Code = db.Column(db.String(10))
    Permit_Type = db.Column(db.String(255))
    Permit_ID = db.Column(db.Integer)
    Permit_Issue_Date = db.Column(db.Date)
    Most_Recent_Test = db.Column(db.Date)
    Previous_Test_Status = db.Column(db.String(255))
    Active_Enforcement_Flag = db.Column(db.Boolean, default=False)

# TestRequests Table
class TestRequest(db.Model):
    Req_ID = db.Column(db.Integer, primary_key=True)
    Source_ID = db.Column(db.Integer, db.ForeignKey('source.Source_ID'), nullable=False)
    Submitted_By = db.Column(db.String(255))
    Date_Sent = db.Column(db.Date)
    Description = db.Column(db.Text)
    Control_Unit = db.Column(db.String(255))
    Emission_Unit = db.Column(db.String(255))
    Rule_Target = db.Column(db.String(255))
    Due_Date = db.Column(db.Date)

# Source_Equipment Table
class SourceEquipment(db.Model):
    Source_ID = db.Column(db.Integer, db.ForeignKey('source.Source_ID'), nullable=False)
    Control_Unit = db.Column(db.String(255))
    Emission_Unit = db.Column(db.String(255))
    Rule_Target = db.Column(db.String(255))
    Emission_Limits = db.Column(db.String(255))
    Initial_Test = db.Column(db.Date)
    Latest_Test = db.Column(db.Date)
    Testing_Period = db.Column(db.String(255))
    Startup_Date = db.Column(db.Date)
    Permit_ID = db.Column(db.Integer)

    __table_args__ = (
        db.PrimaryKeyConstraint('Source_ID', 'Control_Unit', 'Emission_Unit'),
    )

# Test_Protocol Table
class TestProtocol(db.Model):
    Protocol_ID = db.Column(db.Integer, primary_key=True)
    Source_ID = db.Column(db.Integer, db.ForeignKey('source.Source_ID'), nullable=False)
    Request_ID = db.Column(db.Integer, db.ForeignKey('testrequest.Req_ID'))
    Expected_Date = db.Column(db.Date)
    Rule_Target = db.Column(db.String(255))
    Permit_ID = db.Column(db.Integer)
    Description = db.Column(db.Text)
    Control_Unit = db.Column(db.String(255))
    Emission_Unit = db.Column(db.String(255))
    Test_Received_Date = db.Column(db.Date)
    Status = db.Column(db.String(255))
    Reviewed_By = db.Column(db.String(255))

# Test_Inquiries Table
class TestInquiry(db.Model):
    Inquiry_ID = db.Column(db.Integer, primary_key=True)
    Source_ID = db.Column(db.Integer, db.ForeignKey('source.Source_ID'), nullable=False)
    Submitted_By = db.Column(db.String(255))
    Section_of_Origin = db.Column(db.String(255))
    Description = db.Column(db.Text)
    Enforcement_Flag = db.Column(db.Boolean, default=False)
    Control_Unit = db.Column(db.String(255))
    Emission_Unit = db.Column(db.String(255))
    Rule_Target = db.Column(db.String(255))

class TestArchive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, db.ForeignKey('source.Source_ID'), nullable=False)
    protocol_id = db.Column(db.Integer, db.ForeignKey('testprotocol.Protocol_ID'), nullable=True)
    description = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    control_unit = db.Column(db.String(255))
    emission_unit = db.Column(db.String(255))
    request_id = db.Column(db.Integer, db.ForeignKey('testrequests.Req_ID'), nullable=True)
    protocol_date = db.Column(db.Date)
    date_test_performed = db.Column(db.Date)
    date_final_report_due = db.Column(db.Date)
    test_received_date = db.Column(db.Date)
    rule_target = db.Column(db.String(255))
    status = db.Column(db.String(50))
    reviewer = db.Column(db.String(100))

    # Ensure foreign keys reference the correct tables
    __table_args__ = (
        db.ForeignKeyConstraint(['source_id'], ['source.Source_ID']),
        db.ForeignKeyConstraint(['protocol_id'], ['testprotocol.Protocol_ID']),
        db.ForeignKeyConstraint(['request_id'], ['testrequests.Req_ID']),
    )


@app.route("/")
def home():
    return "Hello, Flask is connected to MySQL!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
