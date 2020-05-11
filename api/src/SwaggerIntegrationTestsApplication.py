if __name__ == '__main__' :
    from domain.control import Globals
    globals = Globals.Globals(debugStatus = True)

    import SwaggerIntegrationTests
    mainSwaggerUrl = 'someMainSwaggerUrl'
    swagger = SwaggerIntegrationTests.SwaggerIntegrationTests(globals,mainSwaggerUrl)
    runTestSet = {
        'swaggerTagName' : [
            'swaggerTest_1',
            'swaggerTest_2',
            'swaggerTest_3'
        ],
        'otherSwaggerTagName' : [
            'otherSwaggerTest_1',
            'otherSwaggerTest_2',
            'otherSwaggerTest_3'
        ],
    }
    swagger.runTestSet(runTestSet)
    swagger.closeDriver()
