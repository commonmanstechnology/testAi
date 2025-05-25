```xml
<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/employees">
    <employeesOutput>
      <xsl:for-each select="employee[department='101']">
        <employee>
          <employeeId><xsl:value-of select="employeeId"/></employeeId>
          <employeeName><xsl:value-of select="employeeName"/></employeeName>
          <department><xsl:value-of select="department"/></department>
        </employee>
      </xsl:for-each>
    </employeesOutput>
  </xsl:template>
</xsl:stylesheet>
```