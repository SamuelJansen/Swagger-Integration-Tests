if __name__ == '__main__' :
    from domain.control import Globals
    globals = Globals.Globals(debugStatus = True)

    import SwaggerIntegrationTests
    mainSwaggerUrl = 'someMainSwaggerUrl'
    swagger = SwaggerIntegrationTests.SwaggerIntegrationTests(globals,mainSwaggerUrl)

    runTestSet = {
        'swaggerTagName' : [
            'testNameExample',
            'testCaseNameExample'
        ],
        'otherSwaggerTagName' : [
            'otherTestNameExample',
            'otherTestCaseNameExample'
        ],
    }
    swagger.runTestSet(runTestSet)
    swagger.closeDriver()
