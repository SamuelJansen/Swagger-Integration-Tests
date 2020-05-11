if __name__ == '__main__' :
    from domain.control import Globals
    globals = Globals.Globals(debugStatus = True)

    import SwaggerIntegrationTests
    swagger = SwaggerIntegrationTests.SwaggerIntegrationTests(globals)
    runTestSet = {
        'swaggerTagName' : [
            'swaggerTest_1',
            'swaggerTest_2',
            'swaggerTest_3'
        ],
        'otherSwaggerTagName' : [
            'swaggerTest_1',
            'swaggerTest_2',
            'swaggerTest_3'
        ],
    }
    swagger.runTestSet(runTestSet)
    swagger.closeDriver()
