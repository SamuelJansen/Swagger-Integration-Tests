if __name__ == '__main__' :
    from domain.control import Globals
    globals = Globals.Globals(debugStatus = True)

    import SwaggerIntegrationTests
    swagger = SwaggerIntegrationTests.SwaggerIntegrationTests(globals)

    runTestSet = {
        'Catalog' : [
            'mustCreateCatalogItemPassingOneUnitsInStock',
            'mustCreateCatalogItemNotPassingUnitsInStock',
            'mustCreateCatalogItemPassingZeroUnitsInStock',

            'mustUpdateCatalogItemPassingOneUnitsInStock',
            'mustUpdateCatalogItemNotPassingUnitsInStock',
            'mustUpdateCatalogItemPassingZeroUnitsInStock',

            'mustCreateCatalogItemEmployeeBound',
            'mustCreateCatalogItemEmployeeBoundList'
        ]
    }

    swagger.runTestSet(runTestSet)

    swagger.closeDriver()
