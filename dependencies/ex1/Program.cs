using Bogus;
using Spectre.Console;

public class Program
{
    public static void Main()
    {
        AnsiConsole.Write(new FigletText("Mock Data").Color(Color.Teal));

        var table = new Table().Border(TableBorder.Rounded);
        table.AddColumn("Name");
        table.AddColumn("Email");
        table.AddColumn("Beruf");

        var faker = new Faker("de");

        for (int i = 0; i < 5; i++)
        {
            table.AddRow(
                faker.Name.FullName(),
                faker.Internet.Email(),
                faker.Name.JobTitle()
            );
        }

        AnsiConsole.Write(table);
    }
}
