from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#engine = create_engine('mysql+pymysql://blbadmin:Chickenpotpie1@beerleagueblog.ca/blb')
#Base = declarative_base()
#Base.metadata.reflect(engine)

comp = [{
"competitionId": "c1",
"name": "Mario Cup",
"subject": "Mario Cart",
"description": "May the best nerd win",
"location": "Jason's House",
"public": True,
"results": "[]",
"state": "In Progress",
"participants": [
    {
        "userId": "user1",
        "competitionId": "c1",
        "compRoleId": "c1r1",
        "rank": 1,
        "permissions": {
            "admin": False,
            "judge": False,
            "competitor": True
            }
        },
    {
        "userId": "user2",
        "competitionId": "c1",
        "compRoleId": "c1r2",
        "rank": 2,
        "permissions": {
            "admin": False,
            "judge": False,
            "competitor": True
            }
        },
    {
        "userId": "user3",
        "competitionId": "c1",
        "compRoleId": "c1r3",
        "rank": 3,
        "permissions": {
            "admin": False,
            "judge": False,
            "competitor": True
            }
        },
    {
        "userId": "user4",
        "competitionId": "c1",
        "compRoleId": "c1r4",
        "rank": 4,
        "permissions": {
            "admin": True,
            "judge": True,
            "competitor": True
            }
        }
    ],
"streamURL": "",
"stages": [
        {
            "stageId": "c1s1",
            "name": "Semi Finals",
            "description": "Elimination Round",
            "nextStage": "c1s2",
            "location": "Mario Circut",
            "state": "Completed",
            "seed": [
                1,
                2,
                3,
                4
                ],
            "participants": [
                {
                    "userId": "user1",
                    "stageId": "c1s1",
                    "stageRoleId": "c1s1r1",
                    "rank": 1,
                    "permissions": {
                        "admin": False,
                        "judge": False,
                        "competitor": True
                        }
                    },
                {
                    "userId": "user2",
                    "stageId": "c1s1",
                    "stageRoleId": "c1s1r2",
                    "rank": 2,
                    "permissions": {
                        "admin": False,
                        "judge": False,
                        "competitor": True
                        }
                    },
                {
                    "userId": "user3",
                    "stageId": "c1s1",
                    "stageRoleId": "c1s1r3",
                    "rank": 3,
                    "permissions": {
                        "admin": False,
                        "judge": False,
                        "competitor": True
                        }
                    },
                {
                    "userId": "user4",
                    "stageId": "c1s1",
                    "stageRoleId": "c1s1r4",
                    "rank": 4,
                    "permissions": {
                        "admin": True,
                        "judge": True,
                        "competitor": True
                        }
                    }
                ],
            "results": [
                    "user1",
                    "user3",
                    "user2",
                    "user4"
                    ],
            "event": [
                    {
                        "eventId": "c1s1e1",
                        "name": "Race 1",
                        "location": "Mario Circut",
                        "parentStage": "c1s1",
                        "state": "Completed",
                        "results": [
                            "user1",
                            "user4"
                            ],
                        "seed": [
                            1,
                            4
                            ],
                        "participants": [
                            {
                                "userId": "user1",
                                "eventId": "c1s1e1",
                                "eventRoleId": "c1s1e1r1",
                                "rank": 1,
                                "permissions": {
                                    "admin": False,
                                    "judge": False,
                                    "competitor": True
                                    }
                                },
                            {
                                "userId": "user4",
                                "eventId": "c1s1e1",
                                "eventRoleId": "c1s1e1r2",
                                "rank": 4,
                                "permissions": {
                                    "admin": True,
                                    "judge": True,
                                    "competitor": True
                                    }
                                }
                            ]
                        },
                    {
                        "eventId": "c1s1e2",
                        "name": "Race 1",
                        "location": "Mario Circut",
                        "parentStage": "c1s1",
                        "state": "Completed",
                        "results": [
                            "user3",
                            "user2"
                            ],
                        "seed": [
                            2,
                            3
                            ],
                        "participants": [
                            {
                                "userId": "user2",
                                "eventId": "c1s1e2",
                                "eventRoleId": "c1s1e2r1",
                                "rank": 2,
                                "permissions": {
                                    "admin": False,
                                    "judge": False,
                                    "competitor": True
                                    }
                                },
                            {
                                "userId": "user3",
                                "eventId": "c1s1e3",
                                "eventRoleId": "c1s1e2r2",
                                "rank": 3,
                                "permissions": {
                                    "admin": False,
                                    "judge": False,
                                    "competitor": True
                                    }
                                },
                            {
                                "userId": "user4",
                                "eventId": "c1s1e2",
                                "eventRoleId": "c1s1e2r3",
                                "rank": -1,
                                "permissions": {
                                    "admin": True,
                                    "judge": True,
                                    "competitor": False
                                    }
                                }
                            ]
                        }
                    ],
    "parentCompetition": "c1"
  },
  {
          "stageId": "c1s2",
          "name": "Finals",
          "description": "Winner takes the cup",
          "previousStage": "c1s1",
          "location": "Mario Circut",
          "state": "In Progress",
          "seed": [
              1,
              2
              ],
          "participants": [
              {
                  "userId": "user1",
                  "stageId": "c1s2",
                  "stageRoleId": "c1s2r1",
                  "rank": 1,
                  "permissions": {
                      "admin": False,
                      "judge": False,
                      "competitor": True
                      }
                  },
              {
                  "userId": "user3",
                  "stageId": "c1s2",
                  "stageRoleId": "c1s2r2",
                  "rank": 2,
                  "permissions": {
                      "admin": False,
                      "judge": False,
                      "competitor": True
                      }
                  },
              {
                  "userId": "user4",
                  "stageId": "c1s2",
                  "stageRoleId": "c1s2r3",
                  "rank": -1,
                  "permissions": {
                      "admin": True,
                      "judge": True,
                      "competitor": False
                      }
                  }
              ],
          "results": [],
          "event": [
              {
                  "eventId": "c1s2e1",
                  "name": "Fianl Race",
                  "location": "Mario Circut",
                  "parentStage": "c1s2",
                  "state": "In Progress",
                  "seed": [
                      1,
                      4
                      ],
                  "participants": [
                      {
                          "userId": "user1",
                          "eventId": "c1s2e1",
                          "eventRoleId": "c1s2e1r1",
                          "rank": 1,
                          "permissions": {
                              "admin": False,
                              "judge": False,
                              "competitor": True
                              }
                          },
                      {
                          "userId": "user3",
                          "eventId": "c1s2e1",
                          "eventRoleId": "c1s2e1r2",
                          "rank": 2,
                          "permissions": {
                              "admin": False,
                              "judge": False,
                              "competitor": True
                              }
                          },
                      {
                          "userId": "user4",
                          "eventId": "c1s2e1",
                          "eventRoleId": "c1s2e1r3",
                          "rank": -1,
                          "permissions": {
                              "admin": True,
                              "judge": True,
                              "competitor": False
                              }
                          }
                      ]
                  }
              ],
          "parentCompetition": "c1"
  }
]
}]

app = Flask(__name__, static_url_path="", static_folder="package")

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/competitions/<competition_id>', methods=['GET', 'PUT'])
def competition(competition_id):
    if request.method == 'PUT':
        return "Not yet implemented"
    elif request.method == 'GET':
        return jsonify({'competition': comp[0]})

@app.route('/competitions')
def all_competitions():
    return jsonify({'competitions':comp})

@app.route('/users')
def cook_rating():
    return "Hey look, this is a GET request for users."

if __name__ == '__main__':
    app.run(debug=True)
